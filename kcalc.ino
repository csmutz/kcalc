#include <LiquidCrystal.h>
#include <Keypad.h>
#include <BigNumber.h>

// LCD
const int rs = 19, en = 18, d4 = 17, d5 = 16, d6 = 15, d7 = 14;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
#define LCD_WIDTH 21

//Keypad
const byte ROWS = 4; 
const byte COLS = 4; 

char hexaKeys[ROWS][COLS] = {
  {'1', '2', '3', '/'},
  {'4', '5', '6', 'x'},
  {'7', '8', '9', '-'},
  {'.', '0', '=', '+'}
};

byte rowPins[ROWS] = {6, 7, 8, 9}; 
byte colPins[COLS] = {2, 3, 4, 5}; 

Keypad keypad = Keypad(makeKeymap(hexaKeys), rowPins, colPins, ROWS, COLS); 

//Variables
char operand1[LCD_WIDTH] = "";
char operation[2] = "";
char operand2[LCD_WIDTH] = "";
char solution[LCD_WIDTH] = "Welcome to Kcalc  ";
byte state = 0;
char button[2] = "";

void display() {
    char line[LCD_WIDTH] = "";
    lcd.clear();
    
    snprintf(line, LCD_WIDTH, "%20s", operand1);
    lcd.setCursor(0, 0); 
    lcd.print(line);
    
    lcd.setCursor(19, 1); 
    lcd.print(operation);
    snprintf(line, LCD_WIDTH, "%20s", operand2);
    lcd.setCursor(0, 2); 
    lcd.print(line);
    
    snprintf(line, LCD_WIDTH, "%20s", solution);
    lcd.setCursor(0, 3); 
    lcd.print(line);
  
}

void strip_trailing(char *s) {
  if (strchr(s, '.') == 0) {
    return;
  }
  byte len = strlen(s);
  len--;
  while(s[len] == '0')
  {
    s[len] = 0;
    if (s[len - 1] == '.')
    {
      s[len - 1] = 0;
    }
    len--;
  }
}

void setup() {
  // set up the LCD's number of columns and rows:
  lcd.begin(20, 4);
  keypad.setHoldTime(5);               // Default is 1000mS
  keypad.setDebounceTime(5);           // Default is 50mS
  display();
  button[1] = 0;
  operation[1] = 0;
  state = 0;
  BigNumber::begin(20);
}

void loop() {
  button[0] = keypad.waitForKey();
  if (state == 0) {
    if (button[0] == '0' || button[0] == '1' || button[0] == '1' || button[0] == '2' || button[0] == '3' || button[0] == '4' || button[0] == '5' || button[0] == '6' || button[0] == '7' || button[0] == '8' || button[0] == '9') {
      strlcat(operand1, button, LCD_WIDTH);  
    }
    if (button[0] == '.') {
      if (strchr(operand1, '.') == 0) {
        strlcat(operand1, button, LCD_WIDTH);
      }
    }
    if ((strlen(operand1) > 0 && operand1[0] != '.') || (strlen(operand1) > 1 && operand1[0] == '.')) {
      if (button[0] == '+' || button[0] == '-' || button[0] == 'x' || button[0] == '/') {
        state = 1;
        operation[0] = button[0];
      }
    }
    solution[0] = 0;
  } //end of state 0
  else if (state == 1) {
    if (button[0] == '0' || button[0] == '1' || button[0] == '1' || button[0] == '2' || button[0] == '3' || button[0] == '4' || button[0] == '5' || button[0] == '6' || button[0] == '7' || button[0] == '8' || button[0] == '9') {
      strlcat(operand2, button, LCD_WIDTH);  
    }
    if (button[0] == '.') {
      if (strchr(operand2, '.') == 0) {
        strlcat(operand2, button, LCD_WIDTH);
      }
    }
     if ((strlen(operand2) > 0 && operand2[0] != '.') || (strlen(operand2) > 1 && operand2[0] == '.')) {
       if (button[0] == '=') {
          state = 2;
          //calculate solution
          BigNumber a = operand1;
          BigNumber b = operand2;
          BigNumber c;
    
          if (operation[0] == 'x') {
            c = a * b;
          }
          if (operation[0] == '+') {
            c = a + b;
          }
          if (operation[0] == '-') {
            c = a - b;
          }
          if (operation[0] == '/') {
            //check for divide by zero
            if (b == 0)
            {
              state = 0;
              operand1[0] = 0;
              operation[0] = 0;
              operand2[0] = 0;
              snprintf(solution, LCD_WIDTH, "%s", "ERROR: DIVIDE BY 0!");
            } else { 
              c = a / b;
            }  
            
          }
          if (state == 2)
          {
            char *s = c.toString();
            snprintf(solution, LCD_WIDTH, "%s", s);
            free(s);
            strip_trailing(solution);
          }
      } 
    } 
  } //end of state 1
  else if (state = 2) {
    if (button[0] == '0' || button[0] == '1' || button[0] == '1' || button[0] == '2' || button[0] == '3' || button[0] == '4' || button[0] == '5' || button[0] == '6' || button[0] == '7' || button[0] == '8' || button[0] == '9' || button[0] == '.') {
      state = 0;
      operand1[0] = 0;
      operation[0] = 0;
      operand2[0] = 0;
      solution[0] = 0;
      strlcat(operand1, button, LCD_WIDTH);
    }
    if (button[0] == '+' || button[0] == '-' || button[0] == 'x' || button[0] == '/') {
      state = 1;
      snprintf(operand1, LCD_WIDTH, "%s", solution);
      operation[0] = button[0];
      operand2[0] = 0;
      solution[0] = 0;
    }
  }
  display();
}

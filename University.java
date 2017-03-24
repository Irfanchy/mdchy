/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package javauniversity;

/**
 *
 * @author irfan
 */
public class University {
public void printStatus() {
System.out.println("Welcome to Java University");
System.out.println();
System.out.println("Thank you for using Java University");
 
}
public void createUnits(){
   String[] setName = {"Java programming", "Workplace rules", "Lets play"};
   String[] setCode = {"FIT 1234 ", "FIT 1910 ", "FIT 7868 "};  
   for ( int i= 0; i <setName.length; i++){
       System.out.println(setCode[i] + setName[i]);
}
    }
   public void displayUnits(){
       createUnits();
    }  
}



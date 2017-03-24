/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package javauniversity;
import java.util.Arrays;
/**
 *
 * @author irfan
 */
public class Unit{ //extends javauniversity.University {

    public String name;
    public String code;


public Unit(String name, String code) {

    this.name = name;
    this.code = code;
    
}
public void setName (String name) {

    this.name = name;

}
public void setCode (String code) {

    this.code = code;

}
public String getName () {
    return name;

}

public String getCode () {
    return code;

}

public String getUnitDescription(String name, String code){
            return code+" "+ name;
       
}
}



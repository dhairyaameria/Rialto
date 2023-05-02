import { Schema,models,model } from "mongoose";

const userSchema =new Schema({
    accountId:String,
    address:String,
    age:String,
    annualIncome:String,
    car:String,
    children:String,
    city:String,
    code:String,
    country:String,
    email:String,
    firstName:String,
    gender:String,
    incomeType:String,
    lastName:String,
    maritalStatus:String,
    occupation:String,
    phoneNumber:String,
    userName:String
})

const User = models.user||model('user',userSchema)
export default User;
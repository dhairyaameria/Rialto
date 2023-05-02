import connectMongoose from "../../backend/context/conn";
import {getUsers, postUsers} from "../../backend/controllers"

export default function handler(req ,res){
    connectMongoose().catch(()=> res.status(405).json({error: "Error in connection"}))

    const {method} = req

    switch(method){
        case 'GET':
            getUsers(req,res)
            break;
        case 'POST':
            postUsers(req,res)
            break;
        // case 'PUT':
        //     res.status(200).json({method,name:'PUT request'})
        //     break;
        // case 'DELETE':
        //     res.status(200).json({method,name:'DELETE request'})
        //     break;
        default:
            res.setHeader('Allow',['GET','POST','PUT','DELETE']);
            res.status(405).end('Method ${method} not allowed')
    }

    
}
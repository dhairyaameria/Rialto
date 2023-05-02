import User from '../models/user'

// get: http://localhost:3000/api
export async function getUsers(req,res){
    try{
        const users = await User.find({})

        if(!users) return res.status(404).json({error:"Data not found"})        
        return res.status(200).json(users)
    }catch(error){
        return res.status(404).json({error:"Error while fetching data"})
    }
}

// post: http://localhost:3000/api
export async function postUsers(req,res){
    try{
        const formData = req.body;
        if(!formData) return res.status(404).json({error:"Form data not provided"})
        User.create(formData).then((data)=>{
            return res.status(200).json({data})
        })
    }catch(error){
        return res.status(404).json({error:"Error while posting data"})
    }
}




// User.create(formData, function(err,data){
    // return res.status(404).json({data})
// })
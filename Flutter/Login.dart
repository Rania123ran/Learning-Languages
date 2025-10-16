import "package:flutter/material.dart" ;
import "package:learn/Counter.dart"; 
main(){
  runApp(MyApp()); 
}
class MyApp extends StatefulWidget {
  const MyApp({super.key});

  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
 final _formField = GlobalKey<FormState>();
 final emailController = TextEditingController() ;
 final pwdController = TextEditingController() ;
 String message ="" ;
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "Login",
      home: Scaffold(
        appBar: AppBar(title: Text("Form Page",style: TextStyle(color: Colors.white),),
          backgroundColor: Colors.blueAccent, centerTitle: true,),
        body: Column(
          children: [
            SizedBox(height: 20,),
            Center(child: CircleAvatar(backgroundImage:AssetImage("assets/img_1.png"),radius: 100,)) ,
           Form(
             key: _formField,
               child: Column(
             children: [
               TextFormField(
                 controller: emailController,
                 decoration: InputDecoration(
                   labelText: "Email" ,
                     prefixIcon: Icon(Icons.email),
                     border: OutlineInputBorder() ,
                 ),
                 keyboardType: TextInputType.emailAddress,
                 validator: (val){
                   if(val!.isEmpty)return "veuillez saisir une adresse mail";
                 },
               ),
               SizedBox(height: 20,),
               TextFormField(
                 controller: pwdController,
                 maxLength: 8,
                 obscureText: true,
                 obscuringCharacter: "*",
                 decoration: InputDecoration(
                     labelText: "Password" ,
                     prefixIcon: Icon(Icons.password),
                   border: OutlineInputBorder(),
                 ),
                 validator:(val){
                   if(val!.isEmpty) return "veuillez saisir un mot de passe" ;
                 },
               ) ,
               SizedBox(height: 5,),
               FloatingActionButton(
                   child: Text("Login",style: TextStyle(color: Colors.white),),
                   backgroundColor: Colors.blueAccent,
                 onPressed: () {
                     if (_formField.currentState!.validate()){
                       setState(() {
                         message = "Form validé";
                       });
                     }
                     else{
                       setState(() {
                         message ="Form non validé" ;
                       });
                     }
                 },
                ) ,
               SizedBox(height: 5,),
               Text("${message}",style:TextStyle(color: Colors.red),)
             ],
           ))
          ],
        ),
      ),
    );
  }
}


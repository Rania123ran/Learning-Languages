import "package:flutter/material.dart" ; 
main(){
  runApp(MyApp()) ;
}
class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Resto App',
      home: Scaffold(
        appBar: AppBar(title:Text("Android ATC Pizza Place",style: TextStyle(
          fontStyle: FontStyle.italic , fontSize: 30 , fontFamily: "cursive" ,
          color: Colors.white , fontWeight: FontWeight.bold
        ),), backgroundColor: Colors.orange ) ,
            body: Column(
              children: [
                MyCard(img: "assets/img1.png",name: "Pizza Pepperoni",) ,
                MyCard(img: "assets/img_2.png", name: "Burger") ,
                MyCard(img: "assets/img_3.png", name: "Fries")
              ],
            )
      ),
    );
  }
}
class MyCard extends StatelessWidget {
  final String img ;
  final String name ;
  const MyCard({super.key,required this.img , required this.name});
  @override
  Widget build(BuildContext context) {
    return  Card(
              child: Padding(
                padding: const EdgeInsets.all(8.0),
                child: Row(children: [
                  CircleAvatar(backgroundImage: AssetImage(this.img) ,radius: 40,) ,
                  SizedBox(width: 20,),
                  Text(this.name,style: TextStyle(color: Colors.white,
                  fontSize: 30,fontStyle: FontStyle.italic),)
                ],),
              ),
              color: Colors.orange,
            );
  }
}


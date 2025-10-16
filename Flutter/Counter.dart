import "package:flutter/material.dart" ;
main(){
  runApp(MyApp());
}
class MyApp extends StatefulWidget {
  const MyApp({super.key});

  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  var cnt = 0 ;
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "Counter App",
      home: Scaffold(
        appBar: AppBar(title: Text("Counter App Demo",style: TextStyle(
          color: Colors.white
        ),),),
        body: Center(
          child: Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              FloatingActionButton(onPressed: (){
                setState(() {
                  cnt ++ ;
                });
              } ,
              child: Icon(Icons.add),
                foregroundColor: Colors.white,
                backgroundColor: Colors.blue,
              ),
              SizedBox(width: 20,),
              Text("$cnt",style: TextStyle(fontSize:30),) ,
              SizedBox(width: 20,),
              FloatingActionButton(onPressed: (){
                    setState(() {
                      cnt -- ;
                    });
              } ,
                child: Icon(Icons.minimize),
                foregroundColor: Colors.white,
                backgroundColor: Colors.blue,
              )
            ],
          ),
        ),
      ),
    );
  }
}

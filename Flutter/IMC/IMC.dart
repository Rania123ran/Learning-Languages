import 'package:flutter/material.dart';
import 'Personne.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatefulWidget {
  const MyApp({super.key});

  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  final _formField = GlobalKey<FormState>();
  final poidController = TextEditingController();
  final tailleController = TextEditingController();
  String message = "";
  Color colorValue = Colors.black; // Default color

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "IMC",
      home: Scaffold(
        body: Container(
          padding: EdgeInsets.only(top: 40),
          width: double.infinity,
          decoration: BoxDecoration(
            gradient: LinearGradient(
              begin: Alignment.topCenter,
              colors: [
                Colors.orange[400]!,
                Colors.orange[300]!,
                Colors.orange[200]!,
                Colors.orange[100]!,
              ],
            ),
          ),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.start,
            children: [
              Text(
                "IMC CALCULATOR",
                style: TextStyle(
                  color: Colors.white,
                  fontSize: 35,
                  fontWeight: FontWeight.bold,
                ),
              ),
              Text(
                "contrôlez votre poids",
                style: TextStyle(
                  color: Colors.white,
                  fontSize: 20,
                ),
              ),
              SizedBox(height: 20),
              Expanded(
                child: Container(
                  decoration: BoxDecoration(
                    color: Colors.white,
                    borderRadius: BorderRadius.only(
                      topRight: Radius.circular(50),
                      topLeft: Radius.circular(50),
                    ),
                  ),
                  child: Column(
                    children: [
                      Container(
                        margin: EdgeInsets.only(
                          top: 70,
                          right: 30,
                          left: 30,
                        ),
                        decoration: BoxDecoration(
                          color: Colors.white,
                          borderRadius: BorderRadius.circular(25),
                          boxShadow: [
                            BoxShadow(
                              color: Colors.orange[200]!,
                              offset: Offset.fromDirection(1, 10),
                              blurRadius: 3.0,
                            ),
                          ],
                        ),
                        child: Form(
                          key: _formField,
                          child: Column(
                            children: [
                              TextFormField(
                                controller: poidController,
                                validator: (val) {
                                  if (val!.isEmpty) {
                                    return "Veuillez saisir votre poids";
                                  }
                                  return null;
                                },
                                keyboardType: TextInputType.number,
                                decoration: InputDecoration(
                                  labelText: "Poids en Kg",
                                ),
                              ),
                              SizedBox(height: 20),
                              TextFormField(
                                controller: tailleController,
                                validator: (val) {
                                  if (val!.isEmpty) {
                                    return "Veuillez saisir votre taille";
                                  }
                                  return null;
                                },
                                keyboardType: TextInputType.number,
                                decoration: InputDecoration(
                                  labelText: "Taille en Cm",
                                ),
                              ),
                            ],
                          ),
                        ),
                      ),
                      SizedBox(height: 20),
                      Container(
                        width: 150,
                        child: FloatingActionButton(
                          child: Text("Calculer votre IMC"),
                          backgroundColor: Colors.orange,
                          foregroundColor: Colors.white,
                          onPressed: () {
                            if (_formField.currentState!.validate()) {
                              var p = Personne(
                                poids: double.parse(poidController.text),
                                taille: double.parse(tailleController.text),
                              );
                              var imc = p.Calculer();
                              setState(() {
                                message = p.getMessage(imc);
                                if (imc < 18.6) {
                                  colorValue = Colors.yellow;
                                } else if (imc >= 18.6 && imc <= 29.9) {
                                  colorValue = Colors.green;
                                } else {
                                  colorValue = Colors.orange;
                                }
                              });
                            }
                          },
                        ),
                      ),
                      SizedBox(height: 20),
                      Text(
                        message,
                        style: TextStyle(color: colorValue),
                      ),
                    ],
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

import React, { Component } from "react";

export default class Form0s extends Component {
  constructor(props) {
    super(props);
    this.state = {
      prenom: "",
      nom: "",
      email: "",
      submitted: false, // Pour afficher ou cacher le résumé après soumission
    };
  }

  handleChange = (event) => {
    const { name, value } = event.target;
    this.setState({ [name]: value });
  };

  handleSubmit = (event) => {
    event.preventDefault();
    this.setState({ submitted: true });
  };

  render() {
    const { prenom, nom, email, submitted } = this.state;

    return (
      <div style={{ maxWidth: "400px", margin: "20px auto", fontFamily: "Arial" }}>
        {/* Formulaire */}
        <form
          onSubmit={this.handleSubmit}
          style={{
            padding: "20px",
            border: "1px solid #ddd",
            borderRadius: "5px",
            backgroundColor: "#f9f9f9",
          }}
        >
          <h2 style={{ textAlign: "center", marginBottom: "20px" }}>
            Formulaire de présentation
          </h2>

          <label>Prénom :</label>
          <input
            type="text"
            name="prenom"
            value={prenom}
            onChange={this.handleChange}
            style={{
              width: "100%",
              padding: "8px",
              margin: "10px 0",
              border: "1px solid #ddd",
              borderRadius: "4px",
            }}
          />

          <label>Nom :</label>
          <input
            type="text"
            name="nom"
            value={nom}
            onChange={this.handleChange}
            style={{
              width: "100%",
              padding: "8px",
              margin: "10px 0",
              border: "1px solid #ddd",
              borderRadius: "4px",
            }}
          />

          <label>E-mail :</label>
          <input
            type="email"
            name="email"
            value={email}
            onChange={this.handleChange}
            style={{
              width: "100%",
              padding: "8px",
              margin: "10px 0",
              border: "1px solid #ddd",
              borderRadius: "4px",
            }}
          />

          <button
            type="submit"
            style={{
              width: "100%",
              padding: "10px",
              marginTop: "10px",
              backgroundColor: "#28a745",
              color: "white",
              border: "none",
              borderRadius: "4px",
              cursor: "pointer",
            }}
          >
            Envoyer
          </button>
        </form>

        {/* Résumé des informations */}
        {submitted && (
          <div 
            style={{
              marginTop: "20px",
              padding: "20px",
              border: "1px solid #28a745",
              borderRadius: "5px",
              backgroundColor: "#e9f7e9",
            }}
          >
            <h3 style={{ color: "#28a745" }}>Résumé des informations :</h3>
            <p>
              Prénom : {prenom}, Nom : {nom}, E-mail : {email}
            </p>
          </div>
        )}
      </div>
    );
  }
}

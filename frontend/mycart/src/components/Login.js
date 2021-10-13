import React  from 'react';
import './Login.css'

function Login(){

    return(
        <div className="login">
            <div className="login__container">
                <h1>sign In</h1>
                <form>
                    <h5>E-mail</h5>
                    <input type="email"/>
                    <h5>Password</h5>
                    <input type="password" />
                    <button type="submit" className="login__signInButton">sign In</button>
                </form>
                <p>By signing-in, you agree to Flikcart's Terms and conditions</p>
                <button className="login__registration">create account</button>
            </div>
        </div>
    )

}

export default Login
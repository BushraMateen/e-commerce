import React from 'react';
import SearchIcon from '@mui/icons-material/Search'
import './Header.css'
import { Link } from 'react-router-dom'

function Header() {
    return(
        <nav className="header">
            <div className="header__name">
                <span className="header1">Flikcart</span>
            </div>
            <div className="header__search">
                <input type="text" className="header__search" />
                <SearchIcon className="header__searchIcon" />
            </div>
            <div className="login">
                <Link to = "/" className="header__link">
                <div className="header__option">
                    <span className="header__optionone">login</span>
                </div>
                </Link>
            </div>
        </nav>
    )
}


export default Header
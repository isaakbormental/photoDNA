import React, { Component } from 'react';

import flagAfghan from './img/afghan.png'
import flagAfrican_american from './img/african_american.png'
import flagArgentina from './img/argentina.png'
import flagAustrian from './img/austrian.png'
import flagBrazilian from './img/brazilian.png'
import flagCambodian from './img/cambodian.png'
import flagCanada from './img/canada.png'
import flagChines from './img/chines.png'
import flagCzech from './img/czech.png'
import flagEgipt from './img/egipt.png'
import flagEnglish from './img/english.png'
import flagEthiopian from './img/ethiopian.png'
import flagFilipino from './img/filipino.png'
import flagFrench from './img/french.png'
import flagGerman from './img/german.png'
import flagGreek from './img/greek.png'
import flagHungarian from './img/hungarian.png'
import flagIndian from './img/indian.png'
import flagIndonesia from './img/indonesia.png'
import flagIranian from './img/iranian.png'
import flagIraqi from './img/iraqi.png'
import flagIreland from './img/ireland.png'
import flagIsraeli from './img/israeli.png'
import flagItalian from './img/italian.png'
import flagJapan from './img/japan.png'
import flagKorean from './img/korean.png'
import flagLaos from './img/laos.png'
import flagLatvian from './img/latvian.png'
import flagLituanian from './img/lituanian.png'
import flagMexico from './img/mexico.png'
import flagMongolian from './img/mongolian.png'
import flagNepali from './img/nepali.png'
import flagNigerian from './img/nigerian.png'
import flagPeru from './img/peru.png'
import flagPolish from './img/polish.png'
import flagPuertorican from './img/puertorican.png'
import flagRomanian from './img/romanian.png'
import flagRussian from './img/russian.png'
import flagSamoan from './img/samoan.png'
import flagSaudi from './img/saudi.png'
import flagSerbia from './img/serbia.png'
import flagSouth_african from './img/south_african.png'
import flagSpain from './img/spain.png'
import flagSwedish from './img/swedish.png'
import flagSwiss from './img/swiss.png'
import flagTaiwanese from './img/taiwanese.png'
import flagThai from './img/thai.png'
import flagUkranian from './img/ukrainian.png'
import flagUzbek from './img/uzbek.png'
import flagVietnamese from './img/vietnamese.png'
import flagWelsh from './img/welsh.png'


// TODO: fix flag initing
class Flag extends Component {
    render() {
        let {
            className = 'countryFlag',
            shareCountry,
        } = this.props;

        const flags = {
            "Afghan": flagAfghan,
            "African American": flagAfrican_american,
            "Laotian": flagLaos,
            "Cambodian": flagCambodian,
            "Egyptian": flagEgipt,
            "Chinese": flagChines,
            "English": flagEnglish,
            "Ethiopian": flagEthiopian,
            "Filipino": flagFilipino,
            "French": flagFrench,
            "German": flagGerman,
            "Greek": flagGreek,
            "Hungarian": flagHungarian,
            "Indian": flagIndian,
            "Iranian": flagIranian,
            "Israeli": flagIsraeli,
            "Italian": flagItalian,
            "Japanese": flagJapan,
            "Korean": flagKorean,
            "Latvian": flagLatvian,
            "Lituanian": flagLituanian,
            "Mexican": flagMexico,
            "Mongolian": flagMongolian,
            "Peruvian": flagPeru,
            "Puertorican": flagPuertorican,
            "Romanian": flagRomanian,
            "Russian": flagRussian,
            "Samoan": flagSamoan,
            "Indonesian": flagIndonesia,
            "Spaniard": flagSpain,
            "Swedish": flagSwedish,
            "Swiss": flagSwiss,
            "Taiwanese": flagTaiwanese,
            "Thai": flagThai,
            "Uzbek": flagUzbek,
            "Welsh": flagWelsh,
            "Nigerian": flagNigerian,
            "Austrian": flagAustrian,
            "Brazilian": flagBrazilian,
            "Czech": flagCzech,
            "Iraqi": flagIraqi,
            "Irish": flagIreland,
            "Polish": flagPolish,
            "Saudi Arabian": flagSaudi,
            "Serbian": flagSerbia,
            "South African": flagSouth_african,
            "Nepali": flagNepali,
            "Ukrainian": flagUkranian,
            "Vietnamese": flagVietnamese,
            "Canadian": flagCanada,
            "Argentinian": flagArgentina
        };

        return (
            <img src={flags[shareCountry.name]} className={className} alt=""/>
        );


    }
}

export default Flag;
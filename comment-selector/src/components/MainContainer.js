import React from 'react'
import Checkbox from '@material-ui/core/Checkbox';
import FileSelector from './FileSelector'
import FileDownloader from './FileDownloader';
import UrlGetJSON from './UrlGetJSON';
// import UrlJS from './UrlJS'
import '../components-css/MainContainer.css';
import uparrow from '../images/reddit-uparrow.png';
import downarrow from '../images/reddit-downarrow.png';


class MainContainer extends React.Component{
    state = {
      data: null
    }

    callbackFunction = (childData) => {
      this.setState({data: childData})
    }
    
    handleChecked = (index, e) => {
      let json = this.state.data;
      json.commentsData[index].isChecked = !json.commentsData[index].isChecked;
      this.setState({data: json});
    }
    render() {
      let json = this.state.data
        if(json == null){
            return(
              <div>
                {/* <UrlJS parentCallback = {this.callbackFunction}/> */}
                <UrlGetJSON parentCallback = {this.callbackFunction}/>
                <FileSelector parentCallback = {this.callbackFunction}/>
                <div>no JSON loaded</div>
              </div>
            ) 
        }else{
            const commentHTML = json.commentsData.map((entry,index) => {
              let extraLevelTabs = []
              for(let i = 0; i < entry.level -1; i++){
                  extraLevelTabs.push(<div key={i} className="linestyle"/>)
              }
              return(
                    <div key={index} onClick={(e) => this.handleChecked(index,e)}>
                        
                          <div className="flex-container">
                          <Checkbox checked={entry.isChecked} color='primary'/>
                          {extraLevelTabs}
                            <div className="arrows-and-line">
                              
                              <img src={uparrow} className="votearrow"/>
                              <img src={downarrow} className="votearrow"/>
                              <div className="linestyle"/>
                            </div>
                            <div>
                              <a className="comAuthorstyle">{entry.author}</a>
                              <p className="paragraphstyle"> {entry.body} </p>
                            </div>
                          </div>
                      </div>
                    )
              })
        
        let submissionScore = parseInt(json.submissionData.score);
        console.log(submissionScore);
        if(submissionScore >= 1000){
          submissionScore = (submissionScore/1000).toFixed(1);
          submissionScore = submissionScore + "K";
        }
        
        return (
            <div>
                {/* <UrlJS parentCallback = {this.callbackFunction}/> */}
                <UrlGetJSON parentCallback = {this.callbackFunction}/>
                <FileSelector parentCallback = {this.callbackFunction}/>
                <FileDownloader data={this.state.data}/>
                <div className="flex-container">
                  <div className="arrows-and-line"> 
                      <img src={uparrow} className="votearrow"/>
                      <a className="scorestyle">{submissionScore}</a>
                      <img src={downarrow} className="votearrow"/>
                  </div>
                  <div>
                    <a >{json.submissionData.score}</a>
                    <a className="subAuthorstyle">Posted by u/{json.submissionData.author}</a>
                    <p className="subTitlestyle"> {json.submissionData.title} </p>
                    {/* <p className="paragraphstyle"> {json.submissionData.body} </p> */}
                  </div>
                </div>
                
                    <div>{commentHTML}</div>
            </div>
        );
      }
    }
}

  
export default MainContainer;
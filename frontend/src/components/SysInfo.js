import sysdata from "../out_json_img/sysinfo.json";
import React from "react";
import ReactDOM from "react-dom";
import "../assets/static/css/SysinfoStyle.css";
import ListGroup from "react-bootstrap/ListGroup";

class TableComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      json: null,
    };
  }
  getData = () => {
    fetch("sysinfo.json", {
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
    })
      .then(function (response) {
        return response.json();
      })
      .then(function (result) {
        this.setState({ json: result });
      });
  };
  // componentDidMount() {
  //     this.setState((prevState) => {
  //         return {
  //             json: tampildata()
  //         }
  //     })
  // }

  render() {
    if (this.state.json)
    return (
      <div>
        <table
          style={{
            border: "1px solid black",
          }}
        >
          <tbody style={{ color: "blue" }}>
            <tr>
              <td>Platform</td>
              <td>{this.state.json.platform}</td>
            </tr>
            <tr>
              <td>Platform Release</td>
              <td>{this.state.json.platform_release}</td>
            </tr>
            <tr>
              <td>Platform Version</td>
              <td>{this.state.json.platform_version}</td>
            </tr>
            <tr>
              <td>Processor</td>
              <td>{this.state.json.processor}</td>
            </tr>
            <tr>
              <td>RAM</td>
              <td>{this.state.json.ram}</td>
            </tr>
            {/* {this.state.json.map((data, i) => {
                            return (
                                <tr key={i}>
                                    <td>{data.platform}</td>
                                    <td>{data.lastname}</td>
                                </tr>
                            )
                        })} */}
          </tbody>
        </table>
      </div>
    )
    else
    return (<div>Loading...</div>)
    // return
    // ((this.state.json ? (
    //   <div>Loading...</div>
    // ) : (
    //   <div>
    //     <table
    //       style={{
    //         border: "1px solid black",
    //       }}
    //     >
    //       <tbody style={{ color: "blue" }}>
    //         <tr>
    //           <td>Platform</td>
    //           <td>{this.state.json.platform}</td>
    //         </tr>
    //         <tr>
    //           <td>Platform Release</td>
    //           <td>{this.state.json.platform_release}</td>
    //         </tr>
    //         <tr>
    //           <td>Platform Version</td>
    //           <td>{this.state.json.platform_version}</td>
    //         </tr>
    //         <tr>
    //           <td>Processor</td>
    //           <td>{this.state.json.processor}</td>
    //         </tr>
    //         <tr>
    //           <td>RAM</td>
    //           <td>{this.state.json.ram}</td>
    //         </tr>
    //         {/* {this.state.json.map((data, i) => {
    //                         return (
    //                             <tr key={i}>
    //                                 <td>{data.platform}</td>
    //                                 <td>{data.lastname}</td>
    //                             </tr>
    //                         )
    //                     })} */}
    //       </tbody>
    //     </table>
    //   </div>
    // )));
  }
}

export default TableComponent;

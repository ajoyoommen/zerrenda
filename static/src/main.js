var Item = React.createClass({
  render: function () {
    return (
      <a href="#" className="list-group-item">
        <h4 className="list-group-item-heading">{this.props.name}</h4>
      </a>
    )
  }
});

var List = React.createClass({
  render: function () {
    return (
      <div className="col-md-3">
        <div className="list-group">
          <Item name="do this first"/>
          <Item name="this next"/>
        </div>
      </div>
    )
  }
});

var ToDoComponent = React.createClass({
  render: function () {
    return (
      <div className="row">
        <h3>All your lists</h3>
        <List name="main list"/>
        <List name="no idea"/>
      </div>
    )
  }
});

ReactDOM.render(
  <ToDoComponent />,
  document.getElementById('react-app')
);

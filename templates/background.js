

console.log("================ Background.js connected ==================")
chrome.runtime.onInstalled.addListener(function() {
// creates a listner that listens for the context menu
  chrome.contextMenus.create({
  // creates the context menu item
      "title": "Create Concept Map",
      "contexts": ["selection"],
      "id": "Concept-Map"
  });
});
  
chrome.contextMenus.onClicked.addListener(function(info) {
  
  // runs the code bellow when the context menu item is clicked
    if (info.menuItemId == "Concept-Map" && info.selectionText){
    // the if statement makes sure there is text selected before allowing for the text to be clicked
      console.log(info.selectionText)
      const text = JSON.stringify(info.selectionText)
    }
  })

console.log("================ Background.js ended ==================")
const axios = require("axios")

//An array of Discord Embeds.
let embeds = [
    {
      title: "Discord Webhook Example",
      color: 5174599,
      footer: {
        text: `📅 ${date}`,
      },
      fields: [
        {
          name: "Field Name",
          value: "Field Value"
        },
      ],
    },
  ];

//Stringify the embeds using JSON.stringify()
let data = JSON.stringify({ embeds });

//Create a config object for axios, you can also use axios.post("url", data) instead
var config = {
   method: "POST",
   url: webhook, // https://discord.com/webhook/url/here
   headers: { "Content-Type": "application/json" },
   data: data,
};

//Send the request
 axios(config)
   .then((response) => {
      console.log("Webhook delivered successfully");
      return response;
   })
   .catch((error) => {
     console.log(error);
     return error;
   });

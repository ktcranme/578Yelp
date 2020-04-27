class recPanel {
  //initialize table and select button in panel
  constructor () {
    this.recTable = null;
    this.multiSelect = null;
    this.selectOptions = ['Ethnic Food', 'Food Trucks', 'Specialty Food', 'Imported Food', 'Argentine', 'Food', 'Restaurants', 'Empanadas', 'Pretzels', 'Bakeries', 'Fast Food', 'Vietnamese', 'Soup', 'Burgers', 'Egyptian', 'Middle Eastern', 'Coffee & Tea', 'Cafes', 'Local Flavor', 'Pizza', 'Breakfast & Brunch', 'American (Traditional)', 'Salad', 'Thai', 'Fish & Chips', 'Seafood', 'Ice Cream & Frozen Yogurt', 'Sandwiches', 'Dive Bars', 'Comfort Food', 'Bars', 'Nightlife', 'Italian', 'Hot Dogs', 'Street Vendors', 'Active Life', 'Venues & Event Spaces', 'Mexican', 'Desserts', 'Sushi Bars', 'Chinese', 'Barbeque', 'Southern', 'American (New)', 'Chicken Wings', 'Japanese', 'Dim Sum', 'Vegetarian', 'Ramen', 'Vegan', 'Food Stands', 'Shaved Ice', 'Themed Cafes', 'Shaved Snow', 'Bubble Tea', 'Juice Bars & Smoothies', 'Coffee Roasteries', 'Tapas Bars', 'Gastropubs', 'Cocktail Bars', 'Lounges', 'Wine Bars', 'Internet Cafes', 'Gluten-Free', 'Fruits & Veggies', 'Food Delivery Services', 'Mediterranean', 'Asian Fusion', 'Pubs', 'Sports Bars', 'Beer', 'Wine & Spirits', 'Social Clubs', 'Signature Cuisine', 'Hookah Bars', 'Tex-Mex', 'Fondue', 'Wraps', 'Delis', 'Gelato', 'Tacos', 'Greek', 'African', 'Hotel bar', 'Korean', 'Buffets', 'French', 'Steakhouses', 'Caribbean', 'Breweries', 'Beer Bar', 'Tapas/Small Plates', 'Szechuan', 'Taiwanese', 'Bagels', 'Grocery', 'Indian', 'Noodles', 'Malaysian', 'Teppanyaki', 'Hawaiian', 'Pasta Shops', 'Creperies', 'Cajun/Creole', 'Wineries', 'Falafel', 'German', 'Slovakian', 'Hotels', 'British', 'Cideries', 'Pan Asian', 'Casinos', 'Conveyor Belt Sushi', 'Food Court', 'Cinema', 'Donuts', 'Irish', 'Irish Pub', 'Lebanese', 'Acai Bowls', 'Waffles', 'Tea Rooms', 'Community Service/Non-Profit', 'Soul Food', 'Cheesesteaks', 'Filipino', 'Cantonese', 'Ethiopian', 'Brewpubs', 'Custom Cakes', 'Cupcakes', 'Turkish', 'Diners', 'Indoor Playcentre', 'Latin American', 'Dinner Theater', 'Cafeteria', 'Puerto Rican', 'Spanish', 'Dance Clubs', 'Persian/Iranian', 'Chocolatiers & Shops', 'Macarons', 'Moroccan', 'Poke', 'Speakeasies', 'Beer Gardens', 'Modern European', 'Wine Tasting Room', 'Jazz & Blues', 'Tuscan', 'Brazilian', 'Hot Pot', 'Polish', 'Pakistani', 'Izakaya', 'Brasseries', 'Hong Kong Style Cafe', 'Halal', 'Eatertainment', 'Salvadoran', 'Colombian', 'Do-It-Yourself Food', 'Armenian', 'Laotian', 'Live/Raw Food', 'Piano Bars', 'Comedy Clubs', 'New Mexican Cuisine', 'Dominican', 'Bistros', 'Hungarian', 'Patisserie/Cake Shop', 'Food Banks', 'Popcorn Shops', 'Whiskey Bars', 'Cambodian', 'Venezuelan', 'Himalayan/Nepalese', 'Bangladeshi', 'Herbs & Spices', 'Bed & Breakfast', 'Soba', 'Kebab', 'Japanese Curry', 'Eritrean', 'Smokehouse', 'Farmers Market', 'Kosher', 'Peruvian', 'Portuguese', 'Basque', 'Singaporean', 'Pancakes', 'Cuban', 'Mongolian', 'Arabian', 'DJs', 'Ukrainian', 'Russian', 'Honduran', 'Calabrian', 'Scandinavian', 'Candy Stores', 'Cheese Shops', 'Nicaraguan', 'Grill Services', 'Belgian', 'Botanical Gardens', 'Unofficial Yelp Events', 'Shanghainese', 'Police Departments', 'Tiki Bars', 'Outlet Stores', 'Afghan', 'Game Meat', 'Guamanian', 'Supper Clubs', 'Pop-Up Restaurants', 'Airport Lounges', 'Bar Crawl', 'Honey', 'Chimney Cakes', 'Poutineries', 'Trinidadian', 'Gay Bars', 'Burmese', 'Water Stores', 'Nutritionists', 'Pumpkin Patches', 'Pick Your Own Farms', 'Farms', 'Indonesian', 'Cigar Bars', 'Syrian', 'Bartenders', 'Distilleries', 'Pub Food', 'Czech', 'Polynesian', 'Champagne Bars', 'Pool & Billiards', 'Kombucha', 'Sicilian', 'Delicatessen', 'Cabaret', 'Uzbek', 'Strip Clubs', 'Ski Resorts', 'Wine Tasting Classes', 'Tasting Classes', 'Health Retreats', 'Rotisserie Chicken', 'Club Crawl', 'Airport Terminals', 'Beach Bars', 'Cheese Tasting Classes', 'Wine Tours', 'Beer Garden', 'Coffeeshops', 'Beer Tours', 'Estate Liquidation', 'Catalan', 'Austrian', 'Oaxacan', 'South African', 'Iberian', 'Pita', 'Coffee & Tea Supplies', 'Service Stations', 'Hainan', 'Meaderies'];
  }

  //render datatable for recommended-restaurants
  drawTable = () => {
    this.recTable = $('#rec-table').DataTable({
      data: [],
      columns: [{ data: 'name' }, { data: 'test' }],
      searching: false,
      scrollY: '50vh',
      bInfo: false,
      pageLength: 5,
      scrollCollapse: true,
      language: { emptyTable: 'Please add/change preferences or map view' },
      paging: false,
      ordering: false,
      processing: true
    });
  }

  //when top 10 restaurant is clicked, move map
  restaurantClick = business_id => {
    console.log(business_id);
  }

  //render category select button
  drawSelect = () => {
    var arr = [];
    this.selectOptions.forEach(option => {
      arr.push({ title: option });
    });
    this.multiSelect = $('select').selectize({
      maxItems: null,
      valueField: 'title',
      labelField: 'title',
      searchField: 'title',
      options: arr,
      plugins: ['remove_button'],
      placeholder: 'Type in your interests',
      onChange: val => this.getTopRestaurants(val)
    });
  }

  // get the top restaurants from API on select change
  getTopRestaurants = categories => {
    console.log(categories);
    var test = [];
    categories.forEach(cat => {
      test.push({
        name:
          '<a href="#" onclick="panelObject.restaurantClick(\'' +
          cat +
          '\')">' +
          cat +
          '</a>',
        id: cat,
        test: cat
      })
    });
    this.recTable.clear().draw();
    this.recTable.rows.add(test);
    this.recTable.draw();
  }
}

//draw panels with select and table
document.addEventListener('DOMContentLoaded', () => {
  panelObject = new recPanel();
  panelObject.drawTable();
  panelObject.drawSelect();
})

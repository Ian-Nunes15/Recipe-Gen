from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    response = ""
    
    if request.method == 'POST':
        recipe = request.form.get('recipe_type').lower()
        
        if recipe == "cupcake":
            cupcake = request.form.get('cupcake_type', '').strip().lower()
            if cupcake in ["classic vanilla cupcakes", "vanilla cupcakes"]:
                response = '''Classic Vanilla Cupcake Recipe
Ingredients
For the Cupcakes:
- 1 ½ cups all-purpose flour
- 1 cup granulated sugar
- 1 ½ teaspoons baking powder
- ½ teaspoon baking soda
- ¼ teaspoon salt
- ½ cup unsalted butter, softened
- 2 large eggs, room temperature
- 1 teaspoon pure vanilla extract
- ½ cup whole milk, room temperature

For the Vanilla Frosting:
- ½ cup unsalted butter, softened
- 2 cups powdered sugar
- 1 teaspoon pure vanilla extract
- 2-3 tablespoons heavy cream or milk (adjust for consistency)
- Optional: Sprinkles for decoration

Instructions
1. Preheat the Oven:
   Preheat your oven to 350°F (175°C).
   Line a 12-cup muffin tin with cupcake liners.

2. Make the Cupcake Batter:
   In a large mixing bowl, whisk together the flour, sugar, baking powder, baking soda, and salt.
   Add the softened butter and beat with an electric mixer on low speed until the mixture looks like coarse crumbs.
   In a separate bowl, whisk together the eggs, vanilla extract, and milk.
   Add the wet ingredients to the dry ingredients, mixing until just combined. Do not overmix; the batter should be smooth but not overly beaten.

3. Fill the Cupcake Liners:
   Spoon the batter into the lined muffin tin, filling each cup about two-thirds full.

4. Bake the Cupcakes:
   Bake in the preheated oven for 18-20 minutes or until a toothpick inserted into the center of a cupcake comes out clean.
   Allow the cupcakes to cool in the pan for 5 minutes before transferring them to a wire rack to cool completely.

5. Prepare the Frosting:
   In a mixing bowl, beat the softened butter until creamy and smooth.
   Gradually add the powdered sugar, mixing well after each addition.
   Add the vanilla extract and heavy cream (or milk) and beat on high until the frosting is fluffy and spreadable. Adjust the consistency by adding more powdered sugar (for thicker) or cream (for thinner).

6. Frost and Decorate:
   Once the cupcakes are completely cool, frost them using a piping bag or a spatula.
   Add sprinkles or other decorations if desired.

7. Enjoy:
   Serve and enjoy your delicious Classic Vanilla Cupcakes!
                '''
            elif cupcake == "chocolate cupcakes":
                response = '''Chocolate Cupcake Recipe
Ingredients
For the Cupcakes:
- 1 ½ cups all-purpose flour
- 1 cup granulated sugar
- ½ cup cocoa powder
- 1 ½ teaspoons baking powder
- ½ teaspoon baking soda
- ½ teaspoon salt
- ½ cup unsalted butter, softened
- 2 large eggs
- 1 teaspoon vanilla extract
- ½ cup milk
- ½ cup hot water

For the Chocolate Frosting:
- ½ cup unsalted butter, softened
- 2 cups powdered sugar
- ½ cup cocoa powder
- 2-3 tablespoons milk
- 1 teaspoon vanilla extract

Instructions
1. Preheat the Oven:
   Preheat your oven to 350°F (175°C) and line a muffin tin with cupcake liners.

2. Make the Cupcake Batter:
   In a bowl, mix flour, sugar, cocoa powder, baking powder, baking soda, and salt.
   Add butter and mix until crumbly.
   In another bowl, whisk eggs, vanilla, milk, and hot water.
   Combine wet and dry ingredients until smooth.

3. Fill the Cupcake Liners:
   Fill each liner two-thirds full and bake for 18-20 minutes.

4. Prepare the Frosting:
   Beat butter, then add powdered sugar, cocoa powder, and milk until smooth.

5. Frost and Decorate:
   Frost cooled cupcakes and enjoy!
                '''
            elif cupcake == "red velvet cupcakes":
                response = '''Red Velvet Cupcake Recipe
Ingredients
For the Cupcakes:
- 1 ½ cups all-purpose flour
- 1 cup granulated sugar
- 1 tablespoon cocoa powder
- 1 teaspoon baking soda
- ½ teaspoon salt
- ½ cup unsalted butter, softened
- 2 large eggs
- 1 teaspoon vanilla extract
- 1 cup buttermilk
- 2 teaspoons red food coloring

For the Cream Cheese Frosting:
- ½ cup unsalted butter, softened
- 8 oz cream cheese, softened
- 3 cups powdered sugar
- 1 teaspoon vanilla extract

Instructions
1. Preheat the Oven:
   Preheat your oven to 350°F (175°C) and line a muffin tin with cupcake liners.

2. Make the Cupcake Batter:
   In a bowl, whisk flour, sugar, cocoa powder, baking soda, and salt.
   Add butter and beat until crumbly.
   In another bowl, mix eggs, vanilla, buttermilk, and red food coloring.
   Combine wet and dry ingredients until smooth.

3. Fill the Cupcake Liners:
   Fill each liner two-thirds full and bake for 18-20 minutes.

4. Prepare the Frosting:
   Beat butter and cream cheese, then add powdered sugar and vanilla until smooth.

5. Frost and Decorate:
   Frost cooled cupcakes and enjoy!
                '''
            else:
                response = "Sorry, I don't have that cupcake recipe right now."

        elif recipe == "cookie":
            cookie = request.form.get('cookie_type', '').strip().lower()
            if cookie == "chocolate chip cookies":
                response = '''Chocolate Chip Cookie Recipe
Ingredients
- 1 cup unsalted butter, softened
- 1 cup granulated sugar
- 1 cup brown sugar, packed
- 2 large eggs
- 2 teaspoons vanilla extract
- 3 cups all-purpose flour
- 1 teaspoon baking soda
- ½ teaspoon salt
- 2 cups chocolate chips

Instructions
1. Preheat the Oven:
   Preheat your oven to 350°F (175°C).

2. Make the Cookie Dough:
   In a large bowl, cream together the softened butter, granulated sugar, brown sugar, eggs, and vanilla.
   In another bowl, whisk together the flour, baking soda, and salt.
   Gradually mix the dry ingredients into the wet ingredients until well combined.
   Fold in the chocolate chips.

3. Bake the Cookies:
   Drop spoonfuls of dough onto a lined baking sheet, spacing them about 2 inches apart.
   Bake for 10-12 minutes or until the edges are golden brown.
   Allow the cookies to cool on the baking sheet for a few minutes before transferring them to a wire rack.

4. Enjoy:
   Serve and enjoy your delicious Chocolate Chip Cookies!
                '''
            elif cookie == "oatmeal raisin cookies":
                response = '''Oatmeal Raisin Cookie Recipe
Ingredients
- 1 cup unsalted butter, softened
- 1 cup brown sugar, packed
- 1 cup granulated sugar
- 2 large eggs
- 1 teaspoon vanilla extract
- 1 ½ cups all-purpose flour
- 1 teaspoon baking soda
- ½ teaspoon salt
- 3 cups rolled oats
- 1 cup raisins

Instructions
1. Preheat the Oven:
   Preheat your oven to 350°F (175°C).

2. Make the Cookie Dough:
   In a large bowl, cream together the softened butter, brown sugar, granulated sugar, eggs, and vanilla.
   In another bowl, whisk together the flour, baking soda, and salt.
   Gradually mix the dry ingredients into the wet ingredients.
   Stir in the oats and raisins.

3. Bake the Cookies:
   Drop spoonfuls of dough onto a lined baking sheet and bake for 10-12 minutes until golden brown.
   Cool on a wire rack.

4. Enjoy:
   Serve and enjoy your Oatmeal Raisin Cookies!
                '''
            else:
                response = "Sorry, I don't have that cookie recipe right now."

        elif recipe == "cake":
            cake = request.form.get('cake_type', '').strip().lower()
            if cake == "chocolate cake":
                response = '''Chocolate Cake Recipe
Ingredients
- 1 ¾ cups all-purpose flour
- 2 cups granulated sugar
- ¾ cup cocoa powder
- 1 ½ teaspoons baking powder
- 1 ½ teaspoons baking soda
- 1 teaspoon salt
- 2 large eggs
- 1 cup whole milk
- ½ cup vegetable oil
- 2 teaspoons vanilla extract
- 1 cup boiling water

Instructions
1. Preheat the Oven:
   Preheat your oven to 350°F (175°C). Grease and flour two 9-inch round cake pans.

2. Make the Cake Batter:
   In a large mixing bowl, combine the flour, sugar, cocoa powder, baking powder, baking soda, and salt.
   Add the eggs, milk, oil, and vanilla. Beat for 2 minutes on medium speed.
   Stir in boiling water (batter will be thin).

3. Bake the Cake:
   Pour the batter evenly into the prepared pans.
   Bake for 30-35 minutes, or until a toothpick inserted comes out clean.
   Cool in pans for 10 minutes, then remove from pans and cool completely on a wire rack.

4. Enjoy:
   Frost with your favorite chocolate frosting and enjoy your Chocolate Cake!
                '''
            else:
                response = "Sorry, I don't have that cake recipe right now."

        elif recipe == "pastry":
            pastry = request.form.get('pastry_type', '').strip().lower()
            if pastry == "apple pie":
                response = '''Apple Pie Recipe
Ingredients
For the Pie Crust:
- 2 ½ cups all-purpose flour
- 1 teaspoon salt
- 1 teaspoon sugar
- 1 cup unsalted butter, chilled and diced
- 6 to 8 tablespoons ice water

For the Filling:
- 6 to 8 apples, peeled, cored, and sliced
- ¾ cup sugar
- 2 tablespoons all-purpose flour
- 1 teaspoon cinnamon
- 1 tablespoon lemon juice

Instructions
1. Make the Pie Crust:
   In a bowl, mix flour, salt, and sugar.
   Cut in butter until mixture resembles coarse crumbs.
   Stir in water, one tablespoon at a time, until mixture forms a ball.
   Wrap in plastic and refrigerate for 4 hours or overnight.

2. Prepare the Filling:
   In a large bowl, mix apples, sugar, flour, cinnamon, and lemon juice.

3. Assemble the Pie:
   Preheat the oven to 425°F (220°C).
   Roll out half of the dough to fit a pie pan. Fill with apple mixture and cover with top crust.
   Cut slits for steam to escape. Bake for 15 minutes, then reduce temperature to 350°F (175°C) and bake for 35-45 minutes.

4. Enjoy:
   Let cool before serving your delicious Apple Pie!
                '''
            else:
                response = "Sorry, I don't have that pastry recipe right now."
        else:
            response = "Sorry, I don't have that type of recipe right now."

    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Recipe Generator</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f2f2f2;
                color: #333;
                margin: 0;
                padding: 20px;
            }
            h1, h2, h3, h4 {
                color: red;
            }
            form {
                margin-bottom: 20px;
            }
            label {
                display: block;
                margin-bottom: 10px;
            }
            input[type="text"] {
                padding: 10px;
                width: 300px;
                margin-bottom: 10px;
            }
            input[type="submit"] {
                padding: 10px 15px;
                background-color: red;
                color: white;
                border: none;
                cursor: pointer;
            }
            input[type="submit"]:hover {
                background-color: darkred;
            }
            pre {
                background-color: #fff;
                padding: 10px;
                border: 1px solid #ccc;
                overflow: auto;
                white-space: pre-wrap; /* Wrap long lines */
            }
        </style>
    </head>
    <body>
        <h1>This is your epic RECIPE GENERATOR™</h1>
        <h2>This will generate you multiple recipes at your fingertips</h2>
        <h3>****NOTE****</h3>
        <h4>RECIPE GENERATOR™ is still in its beta phase</h4>

        <form method="POST">
            <label for="recipe_type">What type of recipe do you want? (cupcake, cookie, cake, pastry):</label>
            <input type="text" id="recipe_type" name="recipe_type" required>
            <input type="submit" value="Submit">
        </form>

        {% if response %}
            <div>
                <h3>Recipe:</h3>
                <pre>{{ response }}</pre>
            </div>
        {% endif %}
    </body>
    </html>
    ''', response=response)

if __name__ == '__main__':
    app.run(debug=True)

#[2115. Find All Possible Recipes from Given Supplies](https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/description/) 
+ `Medium`

You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients. The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i]. Ingredients to a recipe may need to be created from other recipes, i.e., ingredients[i] may contain a string that is in recipes.

You are also given a string array supplies containing all the ingredients that you initially have, and you have an infinite supply of all of them.

Return a list of all the recipes that you can create. You may return the answer in any order.

Note that two recipes may contain each other in their ingredients.


+ Example 1:
```
Input: recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]
Output: ["bread"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
```

+ Example 2:
```
Input: recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
```

+ Example 3:
```
Input: recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich","burger"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
We can create "burger" since we have the ingredient "meat" and can create the ingredients "bread" and "sandwich".
```


+ Constraints:
```
n == recipes.length == ingredients.length
1 <= n <= 100
1 <= ingredients[i].length, supplies.length <= 100
1 <= recipes[i].length, ingredients[i][j].length, supplies[k].length <= 10
recipes[i], ingredients[i][j], and supplies[k] consist only of lowercase English letters.
All the values of recipes and supplies combined are unique.
Each ingredients[i] does not contain any duplicate values.
```

# Analysis:
- `ingredients[i]` may contain a string that is in `recipes`
- Cycle dependencies may occur, such as when `recipes[i]` has ingredient `recipes[j]`, `recipes[j]` has ingredient `recipes[k]`, and `recipes[k]` has ingredient `recipes[i]`.

# Solution:
```python {.line-numbers}
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # convert supplies and recipes to new data structures which are query efficient
        supplies = set(supplies)
        recipes_dict = {rec: ingds for rec, ingds in zip(recipes, ingredients)}
        
        # iterate over recipes to find good recipe
        ans, visited = [], dict()
        for rec in recipes_dict:
            if self.goodRecipe(rec, recipes_dict, supplies, visited):
                ans.append(rec)
        return ans

    
    def goodRecipe(self, recipe, recipes_dict, supplies, visited):
        if recipe in visited:
            # if the recipe is wait for judging, there existing loop dependency, fail.
            if visited[recipe] < 0:
                visited[recipe] = 0
            return visited[recipe]
        
        flag, visited[recipe] = 1, -1
        for ingd in recipes_dict[recipe]:
            if ingd in supplies:
                # the ingredient is in supplies.
                continue
            elif ingd in recipes_dict and \
                  self.goodRecipe(ingd, recipes_dict, supplies, visited):
                # the ingredient is another good recipe.
                continue
            else:
                flag = 0
                break
        visited[recipe] = flag
        return visited[recipe]
```

# Oral:
In order to enhace query efficiency, we transform the input data structures, namely recipes and supplies, into a more optimized format. Then, we iterate over the recipes and examine whether they can be created. Since an ingredient can also be a recipe, we maintain a visited loopup table to keep track of the creation status of each recipe. The visited status can be:
```
-1: indicates that the recipe is currently being checked,
 0: signifies that the recipe cannot be created,
 1: indicates that it can be successfully created.
```
When we encounter a recipe during the checking process and find its visited status as `-1`, it implies the presence of cyclic dependencies and the recipe is impossible to create. 


Time complexity: O(N)

Space complexity: O(N)

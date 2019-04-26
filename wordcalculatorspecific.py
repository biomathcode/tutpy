
# Python3 code to find frequency of each word 
# function for calculating the frequency 
def freq(str): 
  
    # break the string into list of words 
    str_list = str.split() 
  
    # gives set of unique words 
    unique_words = set(str_list) 
      
    for words in unique_words : 
        print(words , ' : ', str_list.count(words)) 
  
# driver code 
if __name__ == "__main__": 
      
    str =''' Healthy food
Light food
It should be more rich in electrolytes
Light diet,which should be directly consumed by body
Lots of water especially (coconut)
Nutritional content should be increased and light food should be recommended
Clean food
More hygienic and Homemade food
Outside food should avoided
Purified water in excess to compete with dehydration and proper cooked with no contamination.
Hygienic food
Food
Healthy and clean food
Probiotics must be added with enriched nutrient value.
Low carb / bland food
Purify water
Balance diet
More fluid based diet
Solid food should be avoided
Light diet
Healthy food n boiled water
Light and healthy food should be consumed
Hygienic, healthy food
Lot's of liquid should be given
More of liquids in the diet
Eat and drink healthy and purified food and water
Patient should take more fruits like papaya, chiku.
Heat-cooled water
Person should consume boiled water and food prepared in proper sanitation conditions
Avoid outdoor food
Increased fluid uptake , easily digestible soft food like rice , fruits
He or she should take healthy food with purified water
Bland diet, preferably liquid (Less of fats and more of carbs and proteins)
More nutritious food
Light food
More liquid and protein rich diet
It should be light and more of liquid diet should be promoted
'''.lower()
      
    # calling the freq function 
    freq(str) 

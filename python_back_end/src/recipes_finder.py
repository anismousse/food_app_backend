from typing import Dict, List

import requests

from src.constant import Constant

class RecipesFinder():
	def __init__(self, solr_end_point: str) -> None:
		self._solr_query = f'{solr_end_point}query?q=ingredients:'

	def get_recipes(self, ingredients: str) -> any:
		"""Retrieves the recipes based on the ingredients provided.

		Args:
			ingredients: Ingredients.

		Returns:
			List of recipes that can be made based on the ingredients list
			provided.
		"""
		response =  None

		if len(ingredients) > 0:
			# create the endpoint
			end_point = f'{self._solr_query}\"{ingredients}\"~1000'
			response = requests.get(end_point)

		return self._extract_recipes(response)

	def _extract_recipes(self, response: any) -> any:
		recipes_list = {'recipes': None}
		if response.status_code == Constant.SUCCESS:
			content = response.json()

			# extract response data
			response_data = content.get('response')

			if response_data:
			# extract recipes list
				recipes_list['recipes'] = response_data.get('docs')

		return {'recipes': recipes_list}
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.IndustryPetSpeciesDTO import IndustryPetSpeciesDTO


class AlipayCommercePetSpeciesQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommercePetSpeciesQueryResponse, self).__init__()
        self._species = None

    @property
    def species(self):
        return self._species

    @species.setter
    def species(self, value):
        if isinstance(value, list):
            self._species = list()
            for i in value:
                if isinstance(i, IndustryPetSpeciesDTO):
                    self._species.append(i)
                else:
                    self._species.append(IndustryPetSpeciesDTO.from_alipay_dict(i))

    def parse_response_content(self, response_content):
        response = super(AlipayCommercePetSpeciesQueryResponse, self).parse_response_content(response_content)
        if 'species' in response:
            self.species = response['species']

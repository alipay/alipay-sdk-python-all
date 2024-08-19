#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class IndustryPetSpeciesDTO(object):

    def __init__(self):
        self._pet_species = None
        self._pet_species_code = None
        self._pet_type = None

    @property
    def pet_species(self):
        return self._pet_species

    @pet_species.setter
    def pet_species(self, value):
        self._pet_species = value
    @property
    def pet_species_code(self):
        return self._pet_species_code

    @pet_species_code.setter
    def pet_species_code(self, value):
        self._pet_species_code = value
    @property
    def pet_type(self):
        return self._pet_type

    @pet_type.setter
    def pet_type(self, value):
        self._pet_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.pet_species:
            if hasattr(self.pet_species, 'to_alipay_dict'):
                params['pet_species'] = self.pet_species.to_alipay_dict()
            else:
                params['pet_species'] = self.pet_species
        if self.pet_species_code:
            if hasattr(self.pet_species_code, 'to_alipay_dict'):
                params['pet_species_code'] = self.pet_species_code.to_alipay_dict()
            else:
                params['pet_species_code'] = self.pet_species_code
        if self.pet_type:
            if hasattr(self.pet_type, 'to_alipay_dict'):
                params['pet_type'] = self.pet_type.to_alipay_dict()
            else:
                params['pet_type'] = self.pet_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = IndustryPetSpeciesDTO()
        if 'pet_species' in d:
            o.pet_species = d['pet_species']
        if 'pet_species_code' in d:
            o.pet_species_code = d['pet_species_code']
        if 'pet_type' in d:
            o.pet_type = d['pet_type']
        return o



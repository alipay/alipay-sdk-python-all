#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.IndustryPetPictureDTO import IndustryPetPictureDTO


class AlipayCommercePetMerchantarchiveCreateModel(object):

    def __init__(self):
        self._external_pet_id = None
        self._pet_birthday = None
        self._pet_gender = None
        self._pet_nick = None
        self._pet_no_baby = None
        self._pet_pic_list = None
        self._pet_species = None
        self._pet_species_code = None
        self._pet_type = None

    @property
    def external_pet_id(self):
        return self._external_pet_id

    @external_pet_id.setter
    def external_pet_id(self, value):
        self._external_pet_id = value
    @property
    def pet_birthday(self):
        return self._pet_birthday

    @pet_birthday.setter
    def pet_birthday(self, value):
        self._pet_birthday = value
    @property
    def pet_gender(self):
        return self._pet_gender

    @pet_gender.setter
    def pet_gender(self, value):
        self._pet_gender = value
    @property
    def pet_nick(self):
        return self._pet_nick

    @pet_nick.setter
    def pet_nick(self, value):
        self._pet_nick = value
    @property
    def pet_no_baby(self):
        return self._pet_no_baby

    @pet_no_baby.setter
    def pet_no_baby(self, value):
        self._pet_no_baby = value
    @property
    def pet_pic_list(self):
        return self._pet_pic_list

    @pet_pic_list.setter
    def pet_pic_list(self, value):
        if isinstance(value, list):
            self._pet_pic_list = list()
            for i in value:
                if isinstance(i, IndustryPetPictureDTO):
                    self._pet_pic_list.append(i)
                else:
                    self._pet_pic_list.append(IndustryPetPictureDTO.from_alipay_dict(i))
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
        if self.external_pet_id:
            if hasattr(self.external_pet_id, 'to_alipay_dict'):
                params['external_pet_id'] = self.external_pet_id.to_alipay_dict()
            else:
                params['external_pet_id'] = self.external_pet_id
        if self.pet_birthday:
            if hasattr(self.pet_birthday, 'to_alipay_dict'):
                params['pet_birthday'] = self.pet_birthday.to_alipay_dict()
            else:
                params['pet_birthday'] = self.pet_birthday
        if self.pet_gender:
            if hasattr(self.pet_gender, 'to_alipay_dict'):
                params['pet_gender'] = self.pet_gender.to_alipay_dict()
            else:
                params['pet_gender'] = self.pet_gender
        if self.pet_nick:
            if hasattr(self.pet_nick, 'to_alipay_dict'):
                params['pet_nick'] = self.pet_nick.to_alipay_dict()
            else:
                params['pet_nick'] = self.pet_nick
        if self.pet_no_baby:
            if hasattr(self.pet_no_baby, 'to_alipay_dict'):
                params['pet_no_baby'] = self.pet_no_baby.to_alipay_dict()
            else:
                params['pet_no_baby'] = self.pet_no_baby
        if self.pet_pic_list:
            if isinstance(self.pet_pic_list, list):
                for i in range(0, len(self.pet_pic_list)):
                    element = self.pet_pic_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pet_pic_list[i] = element.to_alipay_dict()
            if hasattr(self.pet_pic_list, 'to_alipay_dict'):
                params['pet_pic_list'] = self.pet_pic_list.to_alipay_dict()
            else:
                params['pet_pic_list'] = self.pet_pic_list
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
        o = AlipayCommercePetMerchantarchiveCreateModel()
        if 'external_pet_id' in d:
            o.external_pet_id = d['external_pet_id']
        if 'pet_birthday' in d:
            o.pet_birthday = d['pet_birthday']
        if 'pet_gender' in d:
            o.pet_gender = d['pet_gender']
        if 'pet_nick' in d:
            o.pet_nick = d['pet_nick']
        if 'pet_no_baby' in d:
            o.pet_no_baby = d['pet_no_baby']
        if 'pet_pic_list' in d:
            o.pet_pic_list = d['pet_pic_list']
        if 'pet_species' in d:
            o.pet_species = d['pet_species']
        if 'pet_species_code' in d:
            o.pet_species_code = d['pet_species_code']
        if 'pet_type' in d:
            o.pet_type = d['pet_type']
        return o



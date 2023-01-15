#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayCommercePetFileQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayCommercePetFileQueryResponse, self).__init__()
        self._birth_date = None
        self._breed = None
        self._category = None
        self._expelled_flag = None
        self._id = None
        self._name = None
        self._pet_certify = None
        self._photo = None
        self._sex = None
        self._sterilization_flag = None
        self._vaccines_flag = None

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value):
        self._birth_date = value
    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        self._breed = value
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value
    @property
    def expelled_flag(self):
        return self._expelled_flag

    @expelled_flag.setter
    def expelled_flag(self, value):
        self._expelled_flag = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def pet_certify(self):
        return self._pet_certify

    @pet_certify.setter
    def pet_certify(self, value):
        self._pet_certify = value
    @property
    def photo(self):
        return self._photo

    @photo.setter
    def photo(self, value):
        if isinstance(value, list):
            self._photo = list()
            for i in value:
                self._photo.append(i)
    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, value):
        self._sex = value
    @property
    def sterilization_flag(self):
        return self._sterilization_flag

    @sterilization_flag.setter
    def sterilization_flag(self, value):
        self._sterilization_flag = value
    @property
    def vaccines_flag(self):
        return self._vaccines_flag

    @vaccines_flag.setter
    def vaccines_flag(self, value):
        self._vaccines_flag = value

    def parse_response_content(self, response_content):
        response = super(AlipayCommercePetFileQueryResponse, self).parse_response_content(response_content)
        if 'birth_date' in response:
            self.birth_date = response['birth_date']
        if 'breed' in response:
            self.breed = response['breed']
        if 'category' in response:
            self.category = response['category']
        if 'expelled_flag' in response:
            self.expelled_flag = response['expelled_flag']
        if 'id' in response:
            self.id = response['id']
        if 'name' in response:
            self.name = response['name']
        if 'pet_certify' in response:
            self.pet_certify = response['pet_certify']
        if 'photo' in response:
            self.photo = response['photo']
        if 'sex' in response:
            self.sex = response['sex']
        if 'sterilization_flag' in response:
            self.sterilization_flag = response['sterilization_flag']
        if 'vaccines_flag' in response:
            self.vaccines_flag = response['vaccines_flag']

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.PetPicData import PetPicData


class AlipayInsSceneInsassetprodPetprofileQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayInsSceneInsassetprodPetprofileQueryResponse, self).__init__()
        self._algorithm_pet_species_code = None
        self._coat_color = None
        self._doc_complete = None
        self._doc_status = None
        self._identify_id = None
        self._nose_print_id = None
        self._nose_print_last_upload_time = None
        self._pet_birthday = None
        self._pet_edit = None
        self._pet_gender = None
        self._pet_id = None
        self._pet_nick = None
        self._pet_no_baby = None
        self._pet_pic_param_list = None
        self._pet_species = None
        self._pet_species_code = None
        self._pet_type = None
        self._policy_status = None

    @property
    def algorithm_pet_species_code(self):
        return self._algorithm_pet_species_code

    @algorithm_pet_species_code.setter
    def algorithm_pet_species_code(self, value):
        self._algorithm_pet_species_code = value
    @property
    def coat_color(self):
        return self._coat_color

    @coat_color.setter
    def coat_color(self, value):
        self._coat_color = value
    @property
    def doc_complete(self):
        return self._doc_complete

    @doc_complete.setter
    def doc_complete(self, value):
        self._doc_complete = value
    @property
    def doc_status(self):
        return self._doc_status

    @doc_status.setter
    def doc_status(self, value):
        self._doc_status = value
    @property
    def identify_id(self):
        return self._identify_id

    @identify_id.setter
    def identify_id(self, value):
        self._identify_id = value
    @property
    def nose_print_id(self):
        return self._nose_print_id

    @nose_print_id.setter
    def nose_print_id(self, value):
        self._nose_print_id = value
    @property
    def nose_print_last_upload_time(self):
        return self._nose_print_last_upload_time

    @nose_print_last_upload_time.setter
    def nose_print_last_upload_time(self, value):
        self._nose_print_last_upload_time = value
    @property
    def pet_birthday(self):
        return self._pet_birthday

    @pet_birthday.setter
    def pet_birthday(self, value):
        self._pet_birthday = value
    @property
    def pet_edit(self):
        return self._pet_edit

    @pet_edit.setter
    def pet_edit(self, value):
        self._pet_edit = value
    @property
    def pet_gender(self):
        return self._pet_gender

    @pet_gender.setter
    def pet_gender(self, value):
        self._pet_gender = value
    @property
    def pet_id(self):
        return self._pet_id

    @pet_id.setter
    def pet_id(self, value):
        self._pet_id = value
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
    def pet_pic_param_list(self):
        return self._pet_pic_param_list

    @pet_pic_param_list.setter
    def pet_pic_param_list(self, value):
        if isinstance(value, list):
            self._pet_pic_param_list = list()
            for i in value:
                if isinstance(i, PetPicData):
                    self._pet_pic_param_list.append(i)
                else:
                    self._pet_pic_param_list.append(PetPicData.from_alipay_dict(i))
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
    @property
    def policy_status(self):
        return self._policy_status

    @policy_status.setter
    def policy_status(self, value):
        self._policy_status = value

    def parse_response_content(self, response_content):
        response = super(AlipayInsSceneInsassetprodPetprofileQueryResponse, self).parse_response_content(response_content)
        if 'algorithm_pet_species_code' in response:
            self.algorithm_pet_species_code = response['algorithm_pet_species_code']
        if 'coat_color' in response:
            self.coat_color = response['coat_color']
        if 'doc_complete' in response:
            self.doc_complete = response['doc_complete']
        if 'doc_status' in response:
            self.doc_status = response['doc_status']
        if 'identify_id' in response:
            self.identify_id = response['identify_id']
        if 'nose_print_id' in response:
            self.nose_print_id = response['nose_print_id']
        if 'nose_print_last_upload_time' in response:
            self.nose_print_last_upload_time = response['nose_print_last_upload_time']
        if 'pet_birthday' in response:
            self.pet_birthday = response['pet_birthday']
        if 'pet_edit' in response:
            self.pet_edit = response['pet_edit']
        if 'pet_gender' in response:
            self.pet_gender = response['pet_gender']
        if 'pet_id' in response:
            self.pet_id = response['pet_id']
        if 'pet_nick' in response:
            self.pet_nick = response['pet_nick']
        if 'pet_no_baby' in response:
            self.pet_no_baby = response['pet_no_baby']
        if 'pet_pic_param_list' in response:
            self.pet_pic_param_list = response['pet_pic_param_list']
        if 'pet_species' in response:
            self.pet_species = response['pet_species']
        if 'pet_species_code' in response:
            self.pet_species_code = response['pet_species_code']
        if 'pet_type' in response:
            self.pet_type = response['pet_type']
        if 'policy_status' in response:
            self.policy_status = response['policy_status']

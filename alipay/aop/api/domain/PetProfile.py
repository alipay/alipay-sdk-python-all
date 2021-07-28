#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.PetPicData import PetPicData


class PetProfile(object):

    def __init__(self):
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


    def to_alipay_dict(self):
        params = dict()
        if self.algorithm_pet_species_code:
            if hasattr(self.algorithm_pet_species_code, 'to_alipay_dict'):
                params['algorithm_pet_species_code'] = self.algorithm_pet_species_code.to_alipay_dict()
            else:
                params['algorithm_pet_species_code'] = self.algorithm_pet_species_code
        if self.coat_color:
            if hasattr(self.coat_color, 'to_alipay_dict'):
                params['coat_color'] = self.coat_color.to_alipay_dict()
            else:
                params['coat_color'] = self.coat_color
        if self.doc_complete:
            if hasattr(self.doc_complete, 'to_alipay_dict'):
                params['doc_complete'] = self.doc_complete.to_alipay_dict()
            else:
                params['doc_complete'] = self.doc_complete
        if self.doc_status:
            if hasattr(self.doc_status, 'to_alipay_dict'):
                params['doc_status'] = self.doc_status.to_alipay_dict()
            else:
                params['doc_status'] = self.doc_status
        if self.identify_id:
            if hasattr(self.identify_id, 'to_alipay_dict'):
                params['identify_id'] = self.identify_id.to_alipay_dict()
            else:
                params['identify_id'] = self.identify_id
        if self.nose_print_id:
            if hasattr(self.nose_print_id, 'to_alipay_dict'):
                params['nose_print_id'] = self.nose_print_id.to_alipay_dict()
            else:
                params['nose_print_id'] = self.nose_print_id
        if self.nose_print_last_upload_time:
            if hasattr(self.nose_print_last_upload_time, 'to_alipay_dict'):
                params['nose_print_last_upload_time'] = self.nose_print_last_upload_time.to_alipay_dict()
            else:
                params['nose_print_last_upload_time'] = self.nose_print_last_upload_time
        if self.pet_birthday:
            if hasattr(self.pet_birthday, 'to_alipay_dict'):
                params['pet_birthday'] = self.pet_birthday.to_alipay_dict()
            else:
                params['pet_birthday'] = self.pet_birthday
        if self.pet_edit:
            if hasattr(self.pet_edit, 'to_alipay_dict'):
                params['pet_edit'] = self.pet_edit.to_alipay_dict()
            else:
                params['pet_edit'] = self.pet_edit
        if self.pet_gender:
            if hasattr(self.pet_gender, 'to_alipay_dict'):
                params['pet_gender'] = self.pet_gender.to_alipay_dict()
            else:
                params['pet_gender'] = self.pet_gender
        if self.pet_id:
            if hasattr(self.pet_id, 'to_alipay_dict'):
                params['pet_id'] = self.pet_id.to_alipay_dict()
            else:
                params['pet_id'] = self.pet_id
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
        if self.pet_pic_param_list:
            if isinstance(self.pet_pic_param_list, list):
                for i in range(0, len(self.pet_pic_param_list)):
                    element = self.pet_pic_param_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.pet_pic_param_list[i] = element.to_alipay_dict()
            if hasattr(self.pet_pic_param_list, 'to_alipay_dict'):
                params['pet_pic_param_list'] = self.pet_pic_param_list.to_alipay_dict()
            else:
                params['pet_pic_param_list'] = self.pet_pic_param_list
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
        if self.policy_status:
            if hasattr(self.policy_status, 'to_alipay_dict'):
                params['policy_status'] = self.policy_status.to_alipay_dict()
            else:
                params['policy_status'] = self.policy_status
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = PetProfile()
        if 'algorithm_pet_species_code' in d:
            o.algorithm_pet_species_code = d['algorithm_pet_species_code']
        if 'coat_color' in d:
            o.coat_color = d['coat_color']
        if 'doc_complete' in d:
            o.doc_complete = d['doc_complete']
        if 'doc_status' in d:
            o.doc_status = d['doc_status']
        if 'identify_id' in d:
            o.identify_id = d['identify_id']
        if 'nose_print_id' in d:
            o.nose_print_id = d['nose_print_id']
        if 'nose_print_last_upload_time' in d:
            o.nose_print_last_upload_time = d['nose_print_last_upload_time']
        if 'pet_birthday' in d:
            o.pet_birthday = d['pet_birthday']
        if 'pet_edit' in d:
            o.pet_edit = d['pet_edit']
        if 'pet_gender' in d:
            o.pet_gender = d['pet_gender']
        if 'pet_id' in d:
            o.pet_id = d['pet_id']
        if 'pet_nick' in d:
            o.pet_nick = d['pet_nick']
        if 'pet_no_baby' in d:
            o.pet_no_baby = d['pet_no_baby']
        if 'pet_pic_param_list' in d:
            o.pet_pic_param_list = d['pet_pic_param_list']
        if 'pet_species' in d:
            o.pet_species = d['pet_species']
        if 'pet_species_code' in d:
            o.pet_species_code = d['pet_species_code']
        if 'pet_type' in d:
            o.pet_type = d['pet_type']
        if 'policy_status' in d:
            o.policy_status = d['policy_status']
        return o



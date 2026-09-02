#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenSpSkillInfoModifyModel(object):

    def __init__(self):
        self._ability_code = None
        self._skill_chinese_name = None
        self._skill_desc = None
        self._skill_file = None
        self._skill_logo_pic = None
        self._support_merchant_type_list = None

    @property
    def ability_code(self):
        return self._ability_code

    @ability_code.setter
    def ability_code(self, value):
        self._ability_code = value
    @property
    def skill_chinese_name(self):
        return self._skill_chinese_name

    @skill_chinese_name.setter
    def skill_chinese_name(self, value):
        self._skill_chinese_name = value
    @property
    def skill_desc(self):
        return self._skill_desc

    @skill_desc.setter
    def skill_desc(self, value):
        self._skill_desc = value
    @property
    def skill_file(self):
        return self._skill_file

    @skill_file.setter
    def skill_file(self, value):
        self._skill_file = value
    @property
    def skill_logo_pic(self):
        return self._skill_logo_pic

    @skill_logo_pic.setter
    def skill_logo_pic(self, value):
        self._skill_logo_pic = value
    @property
    def support_merchant_type_list(self):
        return self._support_merchant_type_list

    @support_merchant_type_list.setter
    def support_merchant_type_list(self, value):
        if isinstance(value, list):
            self._support_merchant_type_list = list()
            for i in value:
                self._support_merchant_type_list.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.ability_code:
            if hasattr(self.ability_code, 'to_alipay_dict'):
                params['ability_code'] = self.ability_code.to_alipay_dict()
            else:
                params['ability_code'] = self.ability_code
        if self.skill_chinese_name:
            if hasattr(self.skill_chinese_name, 'to_alipay_dict'):
                params['skill_chinese_name'] = self.skill_chinese_name.to_alipay_dict()
            else:
                params['skill_chinese_name'] = self.skill_chinese_name
        if self.skill_desc:
            if hasattr(self.skill_desc, 'to_alipay_dict'):
                params['skill_desc'] = self.skill_desc.to_alipay_dict()
            else:
                params['skill_desc'] = self.skill_desc
        if self.skill_file:
            if hasattr(self.skill_file, 'to_alipay_dict'):
                params['skill_file'] = self.skill_file.to_alipay_dict()
            else:
                params['skill_file'] = self.skill_file
        if self.skill_logo_pic:
            if hasattr(self.skill_logo_pic, 'to_alipay_dict'):
                params['skill_logo_pic'] = self.skill_logo_pic.to_alipay_dict()
            else:
                params['skill_logo_pic'] = self.skill_logo_pic
        if self.support_merchant_type_list:
            if isinstance(self.support_merchant_type_list, list):
                for i in range(0, len(self.support_merchant_type_list)):
                    element = self.support_merchant_type_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.support_merchant_type_list[i] = element.to_alipay_dict()
            if hasattr(self.support_merchant_type_list, 'to_alipay_dict'):
                params['support_merchant_type_list'] = self.support_merchant_type_list.to_alipay_dict()
            else:
                params['support_merchant_type_list'] = self.support_merchant_type_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSpSkillInfoModifyModel()
        if 'ability_code' in d:
            o.ability_code = d['ability_code']
        if 'skill_chinese_name' in d:
            o.skill_chinese_name = d['skill_chinese_name']
        if 'skill_desc' in d:
            o.skill_desc = d['skill_desc']
        if 'skill_file' in d:
            o.skill_file = d['skill_file']
        if 'skill_logo_pic' in d:
            o.skill_logo_pic = d['skill_logo_pic']
        if 'support_merchant_type_list' in d:
            o.support_merchant_type_list = d['support_merchant_type_list']
        return o



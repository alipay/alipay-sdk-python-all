#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayDataDataserviceInputparamcheckRainystestQueryModel(object):

    def __init__(self):
        self._boolean_list = None
        self._date_list = None
        self._num_ext_value = None
        self._num_must = None
        self._num_must_list = None
        self._num_optional = None
        self._num_optional_list = None
        self._price_exat_value = None
        self._price_must = None
        self._price_must_list = None
        self._price_optional = None
        self._price_optional_list = None
        self._string_enum = None
        self._string_must = None
        self._string_must_list = None
        self._string_optional = None
        self._string_optional_list = None
        self._string_pattern = None

    @property
    def boolean_list(self):
        return self._boolean_list

    @boolean_list.setter
    def boolean_list(self, value):
        if isinstance(value, list):
            self._boolean_list = list()
            for i in value:
                self._boolean_list.append(i)
    @property
    def date_list(self):
        return self._date_list

    @date_list.setter
    def date_list(self, value):
        if isinstance(value, list):
            self._date_list = list()
            for i in value:
                self._date_list.append(i)
    @property
    def num_ext_value(self):
        return self._num_ext_value

    @num_ext_value.setter
    def num_ext_value(self, value):
        self._num_ext_value = value
    @property
    def num_must(self):
        return self._num_must

    @num_must.setter
    def num_must(self, value):
        self._num_must = value
    @property
    def num_must_list(self):
        return self._num_must_list

    @num_must_list.setter
    def num_must_list(self, value):
        if isinstance(value, list):
            self._num_must_list = list()
            for i in value:
                self._num_must_list.append(i)
    @property
    def num_optional(self):
        return self._num_optional

    @num_optional.setter
    def num_optional(self, value):
        self._num_optional = value
    @property
    def num_optional_list(self):
        return self._num_optional_list

    @num_optional_list.setter
    def num_optional_list(self, value):
        if isinstance(value, list):
            self._num_optional_list = list()
            for i in value:
                self._num_optional_list.append(i)
    @property
    def price_exat_value(self):
        return self._price_exat_value

    @price_exat_value.setter
    def price_exat_value(self, value):
        self._price_exat_value = value
    @property
    def price_must(self):
        return self._price_must

    @price_must.setter
    def price_must(self, value):
        self._price_must = value
    @property
    def price_must_list(self):
        return self._price_must_list

    @price_must_list.setter
    def price_must_list(self, value):
        if isinstance(value, list):
            self._price_must_list = list()
            for i in value:
                self._price_must_list.append(i)
    @property
    def price_optional(self):
        return self._price_optional

    @price_optional.setter
    def price_optional(self, value):
        self._price_optional = value
    @property
    def price_optional_list(self):
        return self._price_optional_list

    @price_optional_list.setter
    def price_optional_list(self, value):
        if isinstance(value, list):
            self._price_optional_list = list()
            for i in value:
                self._price_optional_list.append(i)
    @property
    def string_enum(self):
        return self._string_enum

    @string_enum.setter
    def string_enum(self, value):
        self._string_enum = value
    @property
    def string_must(self):
        return self._string_must

    @string_must.setter
    def string_must(self, value):
        self._string_must = value
    @property
    def string_must_list(self):
        return self._string_must_list

    @string_must_list.setter
    def string_must_list(self, value):
        if isinstance(value, list):
            self._string_must_list = list()
            for i in value:
                self._string_must_list.append(i)
    @property
    def string_optional(self):
        return self._string_optional

    @string_optional.setter
    def string_optional(self, value):
        self._string_optional = value
    @property
    def string_optional_list(self):
        return self._string_optional_list

    @string_optional_list.setter
    def string_optional_list(self, value):
        if isinstance(value, list):
            self._string_optional_list = list()
            for i in value:
                self._string_optional_list.append(i)
    @property
    def string_pattern(self):
        return self._string_pattern

    @string_pattern.setter
    def string_pattern(self, value):
        self._string_pattern = value


    def to_alipay_dict(self):
        params = dict()
        if self.boolean_list:
            if isinstance(self.boolean_list, list):
                for i in range(0, len(self.boolean_list)):
                    element = self.boolean_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.boolean_list[i] = element.to_alipay_dict()
            if hasattr(self.boolean_list, 'to_alipay_dict'):
                params['boolean_list'] = self.boolean_list.to_alipay_dict()
            else:
                params['boolean_list'] = self.boolean_list
        if self.date_list:
            if isinstance(self.date_list, list):
                for i in range(0, len(self.date_list)):
                    element = self.date_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.date_list[i] = element.to_alipay_dict()
            if hasattr(self.date_list, 'to_alipay_dict'):
                params['date_list'] = self.date_list.to_alipay_dict()
            else:
                params['date_list'] = self.date_list
        if self.num_ext_value:
            if hasattr(self.num_ext_value, 'to_alipay_dict'):
                params['num_ext_value'] = self.num_ext_value.to_alipay_dict()
            else:
                params['num_ext_value'] = self.num_ext_value
        if self.num_must:
            if hasattr(self.num_must, 'to_alipay_dict'):
                params['num_must'] = self.num_must.to_alipay_dict()
            else:
                params['num_must'] = self.num_must
        if self.num_must_list:
            if isinstance(self.num_must_list, list):
                for i in range(0, len(self.num_must_list)):
                    element = self.num_must_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.num_must_list[i] = element.to_alipay_dict()
            if hasattr(self.num_must_list, 'to_alipay_dict'):
                params['num_must_list'] = self.num_must_list.to_alipay_dict()
            else:
                params['num_must_list'] = self.num_must_list
        if self.num_optional:
            if hasattr(self.num_optional, 'to_alipay_dict'):
                params['num_optional'] = self.num_optional.to_alipay_dict()
            else:
                params['num_optional'] = self.num_optional
        if self.num_optional_list:
            if isinstance(self.num_optional_list, list):
                for i in range(0, len(self.num_optional_list)):
                    element = self.num_optional_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.num_optional_list[i] = element.to_alipay_dict()
            if hasattr(self.num_optional_list, 'to_alipay_dict'):
                params['num_optional_list'] = self.num_optional_list.to_alipay_dict()
            else:
                params['num_optional_list'] = self.num_optional_list
        if self.price_exat_value:
            if hasattr(self.price_exat_value, 'to_alipay_dict'):
                params['price_exat_value'] = self.price_exat_value.to_alipay_dict()
            else:
                params['price_exat_value'] = self.price_exat_value
        if self.price_must:
            if hasattr(self.price_must, 'to_alipay_dict'):
                params['price_must'] = self.price_must.to_alipay_dict()
            else:
                params['price_must'] = self.price_must
        if self.price_must_list:
            if isinstance(self.price_must_list, list):
                for i in range(0, len(self.price_must_list)):
                    element = self.price_must_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.price_must_list[i] = element.to_alipay_dict()
            if hasattr(self.price_must_list, 'to_alipay_dict'):
                params['price_must_list'] = self.price_must_list.to_alipay_dict()
            else:
                params['price_must_list'] = self.price_must_list
        if self.price_optional:
            if hasattr(self.price_optional, 'to_alipay_dict'):
                params['price_optional'] = self.price_optional.to_alipay_dict()
            else:
                params['price_optional'] = self.price_optional
        if self.price_optional_list:
            if isinstance(self.price_optional_list, list):
                for i in range(0, len(self.price_optional_list)):
                    element = self.price_optional_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.price_optional_list[i] = element.to_alipay_dict()
            if hasattr(self.price_optional_list, 'to_alipay_dict'):
                params['price_optional_list'] = self.price_optional_list.to_alipay_dict()
            else:
                params['price_optional_list'] = self.price_optional_list
        if self.string_enum:
            if hasattr(self.string_enum, 'to_alipay_dict'):
                params['string_enum'] = self.string_enum.to_alipay_dict()
            else:
                params['string_enum'] = self.string_enum
        if self.string_must:
            if hasattr(self.string_must, 'to_alipay_dict'):
                params['string_must'] = self.string_must.to_alipay_dict()
            else:
                params['string_must'] = self.string_must
        if self.string_must_list:
            if isinstance(self.string_must_list, list):
                for i in range(0, len(self.string_must_list)):
                    element = self.string_must_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.string_must_list[i] = element.to_alipay_dict()
            if hasattr(self.string_must_list, 'to_alipay_dict'):
                params['string_must_list'] = self.string_must_list.to_alipay_dict()
            else:
                params['string_must_list'] = self.string_must_list
        if self.string_optional:
            if hasattr(self.string_optional, 'to_alipay_dict'):
                params['string_optional'] = self.string_optional.to_alipay_dict()
            else:
                params['string_optional'] = self.string_optional
        if self.string_optional_list:
            if isinstance(self.string_optional_list, list):
                for i in range(0, len(self.string_optional_list)):
                    element = self.string_optional_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.string_optional_list[i] = element.to_alipay_dict()
            if hasattr(self.string_optional_list, 'to_alipay_dict'):
                params['string_optional_list'] = self.string_optional_list.to_alipay_dict()
            else:
                params['string_optional_list'] = self.string_optional_list
        if self.string_pattern:
            if hasattr(self.string_pattern, 'to_alipay_dict'):
                params['string_pattern'] = self.string_pattern.to_alipay_dict()
            else:
                params['string_pattern'] = self.string_pattern
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceInputparamcheckRainystestQueryModel()
        if 'boolean_list' in d:
            o.boolean_list = d['boolean_list']
        if 'date_list' in d:
            o.date_list = d['date_list']
        if 'num_ext_value' in d:
            o.num_ext_value = d['num_ext_value']
        if 'num_must' in d:
            o.num_must = d['num_must']
        if 'num_must_list' in d:
            o.num_must_list = d['num_must_list']
        if 'num_optional' in d:
            o.num_optional = d['num_optional']
        if 'num_optional_list' in d:
            o.num_optional_list = d['num_optional_list']
        if 'price_exat_value' in d:
            o.price_exat_value = d['price_exat_value']
        if 'price_must' in d:
            o.price_must = d['price_must']
        if 'price_must_list' in d:
            o.price_must_list = d['price_must_list']
        if 'price_optional' in d:
            o.price_optional = d['price_optional']
        if 'price_optional_list' in d:
            o.price_optional_list = d['price_optional_list']
        if 'string_enum' in d:
            o.string_enum = d['string_enum']
        if 'string_must' in d:
            o.string_must = d['string_must']
        if 'string_must_list' in d:
            o.string_must_list = d['string_must_list']
        if 'string_optional' in d:
            o.string_optional = d['string_optional']
        if 'string_optional_list' in d:
            o.string_optional_list = d['string_optional_list']
        if 'string_pattern' in d:
            o.string_pattern = d['string_pattern']
        return o



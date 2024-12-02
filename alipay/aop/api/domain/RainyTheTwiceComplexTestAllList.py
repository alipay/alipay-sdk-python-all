#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RainyTheTwiceComplexTestAllList(object):

    def __init__(self):
        self._bool_list_must = None
        self._bool_must = None
        self._boolean_list_optional = None
        self._boolean_optional = None
        self._date_list_must = None
        self._date_must = None
        self._num_list_must = None
        self._num_must = None
        self._number_list_optional = None
        self._number_optional = None
        self._price_list_must = None
        self._price_must = None
        self._string_list_must = None
        self._string_list_optional = None
        self._string_list_optional_rainy = None
        self._string_must = None
        self._string_optional = None
        self._string_regex_ip = None
        self._string_regex_num = None

    @property
    def bool_list_must(self):
        return self._bool_list_must

    @bool_list_must.setter
    def bool_list_must(self, value):
        if isinstance(value, list):
            self._bool_list_must = list()
            for i in value:
                self._bool_list_must.append(i)
    @property
    def bool_must(self):
        return self._bool_must

    @bool_must.setter
    def bool_must(self, value):
        self._bool_must = value
    @property
    def boolean_list_optional(self):
        return self._boolean_list_optional

    @boolean_list_optional.setter
    def boolean_list_optional(self, value):
        if isinstance(value, list):
            self._boolean_list_optional = list()
            for i in value:
                self._boolean_list_optional.append(i)
    @property
    def boolean_optional(self):
        return self._boolean_optional

    @boolean_optional.setter
    def boolean_optional(self, value):
        self._boolean_optional = value
    @property
    def date_list_must(self):
        return self._date_list_must

    @date_list_must.setter
    def date_list_must(self, value):
        if isinstance(value, list):
            self._date_list_must = list()
            for i in value:
                self._date_list_must.append(i)
    @property
    def date_must(self):
        return self._date_must

    @date_must.setter
    def date_must(self, value):
        self._date_must = value
    @property
    def num_list_must(self):
        return self._num_list_must

    @num_list_must.setter
    def num_list_must(self, value):
        if isinstance(value, list):
            self._num_list_must = list()
            for i in value:
                self._num_list_must.append(i)
    @property
    def num_must(self):
        return self._num_must

    @num_must.setter
    def num_must(self, value):
        self._num_must = value
    @property
    def number_list_optional(self):
        return self._number_list_optional

    @number_list_optional.setter
    def number_list_optional(self, value):
        if isinstance(value, list):
            self._number_list_optional = list()
            for i in value:
                self._number_list_optional.append(i)
    @property
    def number_optional(self):
        return self._number_optional

    @number_optional.setter
    def number_optional(self, value):
        self._number_optional = value
    @property
    def price_list_must(self):
        return self._price_list_must

    @price_list_must.setter
    def price_list_must(self, value):
        if isinstance(value, list):
            self._price_list_must = list()
            for i in value:
                self._price_list_must.append(i)
    @property
    def price_must(self):
        return self._price_must

    @price_must.setter
    def price_must(self, value):
        self._price_must = value
    @property
    def string_list_must(self):
        return self._string_list_must

    @string_list_must.setter
    def string_list_must(self, value):
        if isinstance(value, list):
            self._string_list_must = list()
            for i in value:
                self._string_list_must.append(i)
    @property
    def string_list_optional(self):
        return self._string_list_optional

    @string_list_optional.setter
    def string_list_optional(self, value):
        if isinstance(value, list):
            self._string_list_optional = list()
            for i in value:
                self._string_list_optional.append(i)
    @property
    def string_list_optional_rainy(self):
        return self._string_list_optional_rainy

    @string_list_optional_rainy.setter
    def string_list_optional_rainy(self, value):
        self._string_list_optional_rainy = value
    @property
    def string_must(self):
        return self._string_must

    @string_must.setter
    def string_must(self, value):
        self._string_must = value
    @property
    def string_optional(self):
        return self._string_optional

    @string_optional.setter
    def string_optional(self, value):
        self._string_optional = value
    @property
    def string_regex_ip(self):
        return self._string_regex_ip

    @string_regex_ip.setter
    def string_regex_ip(self, value):
        self._string_regex_ip = value
    @property
    def string_regex_num(self):
        return self._string_regex_num

    @string_regex_num.setter
    def string_regex_num(self, value):
        self._string_regex_num = value


    def to_alipay_dict(self):
        params = dict()
        if self.bool_list_must:
            if isinstance(self.bool_list_must, list):
                for i in range(0, len(self.bool_list_must)):
                    element = self.bool_list_must[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.bool_list_must[i] = element.to_alipay_dict()
            if hasattr(self.bool_list_must, 'to_alipay_dict'):
                params['bool_list_must'] = self.bool_list_must.to_alipay_dict()
            else:
                params['bool_list_must'] = self.bool_list_must
        if self.bool_must:
            if hasattr(self.bool_must, 'to_alipay_dict'):
                params['bool_must'] = self.bool_must.to_alipay_dict()
            else:
                params['bool_must'] = self.bool_must
        if self.boolean_list_optional:
            if isinstance(self.boolean_list_optional, list):
                for i in range(0, len(self.boolean_list_optional)):
                    element = self.boolean_list_optional[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.boolean_list_optional[i] = element.to_alipay_dict()
            if hasattr(self.boolean_list_optional, 'to_alipay_dict'):
                params['boolean_list_optional'] = self.boolean_list_optional.to_alipay_dict()
            else:
                params['boolean_list_optional'] = self.boolean_list_optional
        if self.boolean_optional:
            if hasattr(self.boolean_optional, 'to_alipay_dict'):
                params['boolean_optional'] = self.boolean_optional.to_alipay_dict()
            else:
                params['boolean_optional'] = self.boolean_optional
        if self.date_list_must:
            if isinstance(self.date_list_must, list):
                for i in range(0, len(self.date_list_must)):
                    element = self.date_list_must[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.date_list_must[i] = element.to_alipay_dict()
            if hasattr(self.date_list_must, 'to_alipay_dict'):
                params['date_list_must'] = self.date_list_must.to_alipay_dict()
            else:
                params['date_list_must'] = self.date_list_must
        if self.date_must:
            if hasattr(self.date_must, 'to_alipay_dict'):
                params['date_must'] = self.date_must.to_alipay_dict()
            else:
                params['date_must'] = self.date_must
        if self.num_list_must:
            if isinstance(self.num_list_must, list):
                for i in range(0, len(self.num_list_must)):
                    element = self.num_list_must[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.num_list_must[i] = element.to_alipay_dict()
            if hasattr(self.num_list_must, 'to_alipay_dict'):
                params['num_list_must'] = self.num_list_must.to_alipay_dict()
            else:
                params['num_list_must'] = self.num_list_must
        if self.num_must:
            if hasattr(self.num_must, 'to_alipay_dict'):
                params['num_must'] = self.num_must.to_alipay_dict()
            else:
                params['num_must'] = self.num_must
        if self.number_list_optional:
            if isinstance(self.number_list_optional, list):
                for i in range(0, len(self.number_list_optional)):
                    element = self.number_list_optional[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.number_list_optional[i] = element.to_alipay_dict()
            if hasattr(self.number_list_optional, 'to_alipay_dict'):
                params['number_list_optional'] = self.number_list_optional.to_alipay_dict()
            else:
                params['number_list_optional'] = self.number_list_optional
        if self.number_optional:
            if hasattr(self.number_optional, 'to_alipay_dict'):
                params['number_optional'] = self.number_optional.to_alipay_dict()
            else:
                params['number_optional'] = self.number_optional
        if self.price_list_must:
            if isinstance(self.price_list_must, list):
                for i in range(0, len(self.price_list_must)):
                    element = self.price_list_must[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.price_list_must[i] = element.to_alipay_dict()
            if hasattr(self.price_list_must, 'to_alipay_dict'):
                params['price_list_must'] = self.price_list_must.to_alipay_dict()
            else:
                params['price_list_must'] = self.price_list_must
        if self.price_must:
            if hasattr(self.price_must, 'to_alipay_dict'):
                params['price_must'] = self.price_must.to_alipay_dict()
            else:
                params['price_must'] = self.price_must
        if self.string_list_must:
            if isinstance(self.string_list_must, list):
                for i in range(0, len(self.string_list_must)):
                    element = self.string_list_must[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.string_list_must[i] = element.to_alipay_dict()
            if hasattr(self.string_list_must, 'to_alipay_dict'):
                params['string_list_must'] = self.string_list_must.to_alipay_dict()
            else:
                params['string_list_must'] = self.string_list_must
        if self.string_list_optional:
            if isinstance(self.string_list_optional, list):
                for i in range(0, len(self.string_list_optional)):
                    element = self.string_list_optional[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.string_list_optional[i] = element.to_alipay_dict()
            if hasattr(self.string_list_optional, 'to_alipay_dict'):
                params['string_list_optional'] = self.string_list_optional.to_alipay_dict()
            else:
                params['string_list_optional'] = self.string_list_optional
        if self.string_list_optional_rainy:
            if hasattr(self.string_list_optional_rainy, 'to_alipay_dict'):
                params['string_list_optional_rainy'] = self.string_list_optional_rainy.to_alipay_dict()
            else:
                params['string_list_optional_rainy'] = self.string_list_optional_rainy
        if self.string_must:
            if hasattr(self.string_must, 'to_alipay_dict'):
                params['string_must'] = self.string_must.to_alipay_dict()
            else:
                params['string_must'] = self.string_must
        if self.string_optional:
            if hasattr(self.string_optional, 'to_alipay_dict'):
                params['string_optional'] = self.string_optional.to_alipay_dict()
            else:
                params['string_optional'] = self.string_optional
        if self.string_regex_ip:
            if hasattr(self.string_regex_ip, 'to_alipay_dict'):
                params['string_regex_ip'] = self.string_regex_ip.to_alipay_dict()
            else:
                params['string_regex_ip'] = self.string_regex_ip
        if self.string_regex_num:
            if hasattr(self.string_regex_num, 'to_alipay_dict'):
                params['string_regex_num'] = self.string_regex_num.to_alipay_dict()
            else:
                params['string_regex_num'] = self.string_regex_num
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RainyTheTwiceComplexTestAllList()
        if 'bool_list_must' in d:
            o.bool_list_must = d['bool_list_must']
        if 'bool_must' in d:
            o.bool_must = d['bool_must']
        if 'boolean_list_optional' in d:
            o.boolean_list_optional = d['boolean_list_optional']
        if 'boolean_optional' in d:
            o.boolean_optional = d['boolean_optional']
        if 'date_list_must' in d:
            o.date_list_must = d['date_list_must']
        if 'date_must' in d:
            o.date_must = d['date_must']
        if 'num_list_must' in d:
            o.num_list_must = d['num_list_must']
        if 'num_must' in d:
            o.num_must = d['num_must']
        if 'number_list_optional' in d:
            o.number_list_optional = d['number_list_optional']
        if 'number_optional' in d:
            o.number_optional = d['number_optional']
        if 'price_list_must' in d:
            o.price_list_must = d['price_list_must']
        if 'price_must' in d:
            o.price_must = d['price_must']
        if 'string_list_must' in d:
            o.string_list_must = d['string_list_must']
        if 'string_list_optional' in d:
            o.string_list_optional = d['string_list_optional']
        if 'string_list_optional_rainy' in d:
            o.string_list_optional_rainy = d['string_list_optional_rainy']
        if 'string_must' in d:
            o.string_must = d['string_must']
        if 'string_optional' in d:
            o.string_optional = d['string_optional']
        if 'string_regex_ip' in d:
            o.string_regex_ip = d['string_regex_ip']
        if 'string_regex_num' in d:
            o.string_regex_num = d['string_regex_num']
        return o



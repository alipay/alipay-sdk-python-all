#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse
from alipay.aop.api.domain.RainyTheTwiceComplexTestAllList import RainyTheTwiceComplexTestAllList
from alipay.aop.api.domain.RainyTheTwiceComplexTestAll import RainyTheTwiceComplexTestAll


class AlipayDataDataexchangeSchemainputparamRainythetwiceQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataexchangeSchemainputparamRainythetwiceQueryResponse, self).__init__()
        self._bool_list_must = None
        self._bool_must = None
        self._boolean_list_optional = None
        self._boolean_optional = None
        self._complex_list_must = None
        self._complex_must = None
        self._date_list_must = None
        self._date_must = None
        self._num_list_must = None
        self._num_must = None
        self._number_list_optional = None
        self._number_optional = None
        self._price_list_must = None
        self._price_list_optional = None
        self._price_must = None
        self._price_optional = None
        self._string_list_must = None
        self._string_list_optional = None
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
    def complex_list_must(self):
        return self._complex_list_must

    @complex_list_must.setter
    def complex_list_must(self, value):
        if isinstance(value, list):
            self._complex_list_must = list()
            for i in value:
                if isinstance(i, RainyTheTwiceComplexTestAllList):
                    self._complex_list_must.append(i)
                else:
                    self._complex_list_must.append(RainyTheTwiceComplexTestAllList.from_alipay_dict(i))
    @property
    def complex_must(self):
        return self._complex_must

    @complex_must.setter
    def complex_must(self, value):
        if isinstance(value, RainyTheTwiceComplexTestAll):
            self._complex_must = value
        else:
            self._complex_must = RainyTheTwiceComplexTestAll.from_alipay_dict(value)
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
    def price_list_optional(self):
        return self._price_list_optional

    @price_list_optional.setter
    def price_list_optional(self, value):
        if isinstance(value, list):
            self._price_list_optional = list()
            for i in value:
                self._price_list_optional.append(i)
    @property
    def price_must(self):
        return self._price_must

    @price_must.setter
    def price_must(self, value):
        self._price_must = value
    @property
    def price_optional(self):
        return self._price_optional

    @price_optional.setter
    def price_optional(self, value):
        self._price_optional = value
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

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataexchangeSchemainputparamRainythetwiceQueryResponse, self).parse_response_content(response_content)
        if 'bool_list_must' in response:
            self.bool_list_must = response['bool_list_must']
        if 'bool_must' in response:
            self.bool_must = response['bool_must']
        if 'boolean_list_optional' in response:
            self.boolean_list_optional = response['boolean_list_optional']
        if 'boolean_optional' in response:
            self.boolean_optional = response['boolean_optional']
        if 'complex_list_must' in response:
            self.complex_list_must = response['complex_list_must']
        if 'complex_must' in response:
            self.complex_must = response['complex_must']
        if 'date_list_must' in response:
            self.date_list_must = response['date_list_must']
        if 'date_must' in response:
            self.date_must = response['date_must']
        if 'num_list_must' in response:
            self.num_list_must = response['num_list_must']
        if 'num_must' in response:
            self.num_must = response['num_must']
        if 'number_list_optional' in response:
            self.number_list_optional = response['number_list_optional']
        if 'number_optional' in response:
            self.number_optional = response['number_optional']
        if 'price_list_must' in response:
            self.price_list_must = response['price_list_must']
        if 'price_list_optional' in response:
            self.price_list_optional = response['price_list_optional']
        if 'price_must' in response:
            self.price_must = response['price_must']
        if 'price_optional' in response:
            self.price_optional = response['price_optional']
        if 'string_list_must' in response:
            self.string_list_must = response['string_list_must']
        if 'string_list_optional' in response:
            self.string_list_optional = response['string_list_optional']
        if 'string_must' in response:
            self.string_must = response['string_must']
        if 'string_optional' in response:
            self.string_optional = response['string_optional']
        if 'string_regex_ip' in response:
            self.string_regex_ip = response['string_regex_ip']
        if 'string_regex_num' in response:
            self.string_regex_num = response['string_regex_num']

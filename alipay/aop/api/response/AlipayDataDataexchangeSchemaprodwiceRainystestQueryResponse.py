#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.response.AlipayResponse import AlipayResponse


class AlipayDataDataexchangeSchemaprodwiceRainystestQueryResponse(AlipayResponse):

    def __init__(self):
        super(AlipayDataDataexchangeSchemaprodwiceRainystestQueryResponse, self).__init__()
        self._boolean_01_n_select_one = None
        self._boolean_02_n_select_one = None
        self._date_01_n_select_one = None
        self._date_02_n_select_one = None
        self._num_01_n_select_one = None
        self._num_02_n_select_one = None
        self._price_01_n_select_one = None
        self._price_02_n_select_one = None
        self._result = None
        self._string_01_n_select_one = None
        self._string_02_n_select_one = None

    @property
    def boolean_01_n_select_one(self):
        return self._boolean_01_n_select_one

    @boolean_01_n_select_one.setter
    def boolean_01_n_select_one(self, value):
        self._boolean_01_n_select_one = value
    @property
    def boolean_02_n_select_one(self):
        return self._boolean_02_n_select_one

    @boolean_02_n_select_one.setter
    def boolean_02_n_select_one(self, value):
        if isinstance(value, list):
            self._boolean_02_n_select_one = list()
            for i in value:
                self._boolean_02_n_select_one.append(i)
    @property
    def date_01_n_select_one(self):
        return self._date_01_n_select_one

    @date_01_n_select_one.setter
    def date_01_n_select_one(self, value):
        self._date_01_n_select_one = value
    @property
    def date_02_n_select_one(self):
        return self._date_02_n_select_one

    @date_02_n_select_one.setter
    def date_02_n_select_one(self, value):
        if isinstance(value, list):
            self._date_02_n_select_one = list()
            for i in value:
                self._date_02_n_select_one.append(i)
    @property
    def num_01_n_select_one(self):
        return self._num_01_n_select_one

    @num_01_n_select_one.setter
    def num_01_n_select_one(self, value):
        self._num_01_n_select_one = value
    @property
    def num_02_n_select_one(self):
        return self._num_02_n_select_one

    @num_02_n_select_one.setter
    def num_02_n_select_one(self, value):
        if isinstance(value, list):
            self._num_02_n_select_one = list()
            for i in value:
                self._num_02_n_select_one.append(i)
    @property
    def price_01_n_select_one(self):
        return self._price_01_n_select_one

    @price_01_n_select_one.setter
    def price_01_n_select_one(self, value):
        self._price_01_n_select_one = value
    @property
    def price_02_n_select_one(self):
        return self._price_02_n_select_one

    @price_02_n_select_one.setter
    def price_02_n_select_one(self, value):
        if isinstance(value, list):
            self._price_02_n_select_one = list()
            for i in value:
                self._price_02_n_select_one.append(i)
    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self._result = value
    @property
    def string_01_n_select_one(self):
        return self._string_01_n_select_one

    @string_01_n_select_one.setter
    def string_01_n_select_one(self, value):
        self._string_01_n_select_one = value
    @property
    def string_02_n_select_one(self):
        return self._string_02_n_select_one

    @string_02_n_select_one.setter
    def string_02_n_select_one(self, value):
        if isinstance(value, list):
            self._string_02_n_select_one = list()
            for i in value:
                self._string_02_n_select_one.append(i)

    def parse_response_content(self, response_content):
        response = super(AlipayDataDataexchangeSchemaprodwiceRainystestQueryResponse, self).parse_response_content(response_content)
        if 'boolean_01_n_select_one' in response:
            self.boolean_01_n_select_one = response['boolean_01_n_select_one']
        if 'boolean_02_n_select_one' in response:
            self.boolean_02_n_select_one = response['boolean_02_n_select_one']
        if 'date_01_n_select_one' in response:
            self.date_01_n_select_one = response['date_01_n_select_one']
        if 'date_02_n_select_one' in response:
            self.date_02_n_select_one = response['date_02_n_select_one']
        if 'num_01_n_select_one' in response:
            self.num_01_n_select_one = response['num_01_n_select_one']
        if 'num_02_n_select_one' in response:
            self.num_02_n_select_one = response['num_02_n_select_one']
        if 'price_01_n_select_one' in response:
            self.price_01_n_select_one = response['price_01_n_select_one']
        if 'price_02_n_select_one' in response:
            self.price_02_n_select_one = response['price_02_n_select_one']
        if 'result' in response:
            self.result = response['result']
        if 'string_01_n_select_one' in response:
            self.string_01_n_select_one = response['string_01_n_select_one']
        if 'string_02_n_select_one' in response:
            self.string_02_n_select_one = response['string_02_n_select_one']

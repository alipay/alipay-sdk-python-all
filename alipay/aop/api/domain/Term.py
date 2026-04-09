#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.Faculty import Faculty


class Term(object):

    def __init__(self):
        self._faculty_list = None
        self._pinyin = None
        self._synonyms = None
        self._term_id = None
        self._term_name = None
        self._type = None

    @property
    def faculty_list(self):
        return self._faculty_list

    @faculty_list.setter
    def faculty_list(self, value):
        if isinstance(value, list):
            self._faculty_list = list()
            for i in value:
                if isinstance(i, Faculty):
                    self._faculty_list.append(i)
                else:
                    self._faculty_list.append(Faculty.from_alipay_dict(i))
    @property
    def pinyin(self):
        return self._pinyin

    @pinyin.setter
    def pinyin(self, value):
        self._pinyin = value
    @property
    def synonyms(self):
        return self._synonyms

    @synonyms.setter
    def synonyms(self, value):
        self._synonyms = value
    @property
    def term_id(self):
        return self._term_id

    @term_id.setter
    def term_id(self, value):
        self._term_id = value
    @property
    def term_name(self):
        return self._term_name

    @term_name.setter
    def term_name(self, value):
        self._term_name = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.faculty_list:
            if isinstance(self.faculty_list, list):
                for i in range(0, len(self.faculty_list)):
                    element = self.faculty_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.faculty_list[i] = element.to_alipay_dict()
            if hasattr(self.faculty_list, 'to_alipay_dict'):
                params['faculty_list'] = self.faculty_list.to_alipay_dict()
            else:
                params['faculty_list'] = self.faculty_list
        if self.pinyin:
            if hasattr(self.pinyin, 'to_alipay_dict'):
                params['pinyin'] = self.pinyin.to_alipay_dict()
            else:
                params['pinyin'] = self.pinyin
        if self.synonyms:
            if hasattr(self.synonyms, 'to_alipay_dict'):
                params['synonyms'] = self.synonyms.to_alipay_dict()
            else:
                params['synonyms'] = self.synonyms
        if self.term_id:
            if hasattr(self.term_id, 'to_alipay_dict'):
                params['term_id'] = self.term_id.to_alipay_dict()
            else:
                params['term_id'] = self.term_id
        if self.term_name:
            if hasattr(self.term_name, 'to_alipay_dict'):
                params['term_name'] = self.term_name.to_alipay_dict()
            else:
                params['term_name'] = self.term_name
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Term()
        if 'faculty_list' in d:
            o.faculty_list = d['faculty_list']
        if 'pinyin' in d:
            o.pinyin = d['pinyin']
        if 'synonyms' in d:
            o.synonyms = d['synonyms']
        if 'term_id' in d:
            o.term_id = d['term_id']
        if 'term_name' in d:
            o.term_name = d['term_name']
        if 'type' in d:
            o.type = d['type']
        return o



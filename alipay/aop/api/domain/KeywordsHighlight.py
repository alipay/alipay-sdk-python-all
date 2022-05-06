#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KeywordsHighlight(object):

    def __init__(self):
        self._searchable_text = None
        self._summary = None
        self._title = None

    @property
    def searchable_text(self):
        return self._searchable_text

    @searchable_text.setter
    def searchable_text(self, value):
        if isinstance(value, list):
            self._searchable_text = list()
            for i in value:
                self._searchable_text.append(i)
    @property
    def summary(self):
        return self._summary

    @summary.setter
    def summary(self, value):
        if isinstance(value, list):
            self._summary = list()
            for i in value:
                self._summary.append(i)
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value, list):
            self._title = list()
            for i in value:
                self._title.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.searchable_text:
            if isinstance(self.searchable_text, list):
                for i in range(0, len(self.searchable_text)):
                    element = self.searchable_text[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.searchable_text[i] = element.to_alipay_dict()
            if hasattr(self.searchable_text, 'to_alipay_dict'):
                params['searchable_text'] = self.searchable_text.to_alipay_dict()
            else:
                params['searchable_text'] = self.searchable_text
        if self.summary:
            if isinstance(self.summary, list):
                for i in range(0, len(self.summary)):
                    element = self.summary[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.summary[i] = element.to_alipay_dict()
            if hasattr(self.summary, 'to_alipay_dict'):
                params['summary'] = self.summary.to_alipay_dict()
            else:
                params['summary'] = self.summary
        if self.title:
            if isinstance(self.title, list):
                for i in range(0, len(self.title)):
                    element = self.title[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.title[i] = element.to_alipay_dict()
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KeywordsHighlight()
        if 'searchable_text' in d:
            o.searchable_text = d['searchable_text']
        if 'summary' in d:
            o.summary = d['summary']
        if 'title' in d:
            o.title = d['title']
        return o



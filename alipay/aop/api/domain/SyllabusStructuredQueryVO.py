#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SyllabusStructuredQueryVO(object):

    def __init__(self):
        self._chapter = None
        self._sections = None

    @property
    def chapter(self):
        return self._chapter

    @chapter.setter
    def chapter(self, value):
        self._chapter = value
    @property
    def sections(self):
        return self._sections

    @sections.setter
    def sections(self, value):
        if isinstance(value, list):
            self._sections = list()
            for i in value:
                self._sections.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.chapter:
            if hasattr(self.chapter, 'to_alipay_dict'):
                params['chapter'] = self.chapter.to_alipay_dict()
            else:
                params['chapter'] = self.chapter
        if self.sections:
            if isinstance(self.sections, list):
                for i in range(0, len(self.sections)):
                    element = self.sections[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sections[i] = element.to_alipay_dict()
            if hasattr(self.sections, 'to_alipay_dict'):
                params['sections'] = self.sections.to_alipay_dict()
            else:
                params['sections'] = self.sections
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SyllabusStructuredQueryVO()
        if 'chapter' in d:
            o.chapter = d['chapter']
        if 'sections' in d:
            o.sections = d['sections']
        return o



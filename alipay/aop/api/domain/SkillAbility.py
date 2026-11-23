#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class SkillAbility(object):

    def __init__(self):
        self._download_url = None
        self._file_name = None
        self._skill_md = None

    @property
    def download_url(self):
        return self._download_url

    @download_url.setter
    def download_url(self, value):
        self._download_url = value
    @property
    def file_name(self):
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value
    @property
    def skill_md(self):
        return self._skill_md

    @skill_md.setter
    def skill_md(self, value):
        self._skill_md = value


    def to_alipay_dict(self):
        params = dict()
        if self.download_url:
            if hasattr(self.download_url, 'to_alipay_dict'):
                params['download_url'] = self.download_url.to_alipay_dict()
            else:
                params['download_url'] = self.download_url
        if self.file_name:
            if hasattr(self.file_name, 'to_alipay_dict'):
                params['file_name'] = self.file_name.to_alipay_dict()
            else:
                params['file_name'] = self.file_name
        if self.skill_md:
            if hasattr(self.skill_md, 'to_alipay_dict'):
                params['skill_md'] = self.skill_md.to_alipay_dict()
            else:
                params['skill_md'] = self.skill_md
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = SkillAbility()
        if 'download_url' in d:
            o.download_url = d['download_url']
        if 'file_name' in d:
            o.file_name = d['file_name']
        if 'skill_md' in d:
            o.skill_md = d['skill_md']
        return o



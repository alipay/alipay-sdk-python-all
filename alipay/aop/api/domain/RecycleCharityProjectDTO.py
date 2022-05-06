#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RecycleCharityProjectDTO(object):

    def __init__(self):
        self._pic_big = None
        self._project_id = None
        self._project_link = None
        self._project_title = None
        self._subject = None

    @property
    def pic_big(self):
        return self._pic_big

    @pic_big.setter
    def pic_big(self, value):
        self._pic_big = value
    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value
    @property
    def project_link(self):
        return self._project_link

    @project_link.setter
    def project_link(self, value):
        self._project_link = value
    @property
    def project_title(self):
        return self._project_title

    @project_title.setter
    def project_title(self, value):
        self._project_title = value
    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value


    def to_alipay_dict(self):
        params = dict()
        if self.pic_big:
            if hasattr(self.pic_big, 'to_alipay_dict'):
                params['pic_big'] = self.pic_big.to_alipay_dict()
            else:
                params['pic_big'] = self.pic_big
        if self.project_id:
            if hasattr(self.project_id, 'to_alipay_dict'):
                params['project_id'] = self.project_id.to_alipay_dict()
            else:
                params['project_id'] = self.project_id
        if self.project_link:
            if hasattr(self.project_link, 'to_alipay_dict'):
                params['project_link'] = self.project_link.to_alipay_dict()
            else:
                params['project_link'] = self.project_link
        if self.project_title:
            if hasattr(self.project_title, 'to_alipay_dict'):
                params['project_title'] = self.project_title.to_alipay_dict()
            else:
                params['project_title'] = self.project_title
        if self.subject:
            if hasattr(self.subject, 'to_alipay_dict'):
                params['subject'] = self.subject.to_alipay_dict()
            else:
                params['subject'] = self.subject
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RecycleCharityProjectDTO()
        if 'pic_big' in d:
            o.pic_big = d['pic_big']
        if 'project_id' in d:
            o.project_id = d['project_id']
        if 'project_link' in d:
            o.project_link = d['project_link']
        if 'project_title' in d:
            o.project_title = d['project_title']
        if 'subject' in d:
            o.subject = d['subject']
        return o



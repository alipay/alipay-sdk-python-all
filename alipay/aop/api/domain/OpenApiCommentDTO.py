#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.OpenApiPersonSaDTO import OpenApiPersonSaDTO


class OpenApiCommentDTO(object):

    def __init__(self):
        self._comment = None
        self._confirm_date = None
        self._confirm_type = None
        self._people = None

    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, value):
        self._comment = value
    @property
    def confirm_date(self):
        return self._confirm_date

    @confirm_date.setter
    def confirm_date(self, value):
        self._confirm_date = value
    @property
    def confirm_type(self):
        return self._confirm_type

    @confirm_type.setter
    def confirm_type(self, value):
        self._confirm_type = value
    @property
    def people(self):
        return self._people

    @people.setter
    def people(self, value):
        if isinstance(value, OpenApiPersonSaDTO):
            self._people = value
        else:
            self._people = OpenApiPersonSaDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.comment:
            if hasattr(self.comment, 'to_alipay_dict'):
                params['comment'] = self.comment.to_alipay_dict()
            else:
                params['comment'] = self.comment
        if self.confirm_date:
            if hasattr(self.confirm_date, 'to_alipay_dict'):
                params['confirm_date'] = self.confirm_date.to_alipay_dict()
            else:
                params['confirm_date'] = self.confirm_date
        if self.confirm_type:
            if hasattr(self.confirm_type, 'to_alipay_dict'):
                params['confirm_type'] = self.confirm_type.to_alipay_dict()
            else:
                params['confirm_type'] = self.confirm_type
        if self.people:
            if hasattr(self.people, 'to_alipay_dict'):
                params['people'] = self.people.to_alipay_dict()
            else:
                params['people'] = self.people
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = OpenApiCommentDTO()
        if 'comment' in d:
            o.comment = d['comment']
        if 'confirm_date' in d:
            o.confirm_date = d['confirm_date']
        if 'confirm_type' in d:
            o.confirm_type = d['confirm_type']
        if 'people' in d:
            o.people = d['people']
        return o



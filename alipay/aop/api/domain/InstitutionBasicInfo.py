#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InstitutionBasicInfo(object):

    def __init__(self):
        self._consult_mode = None
        self._effective = None
        self._effective_end_date = None
        self._effective_start_date = None
        self._institution_desc = None
        self._institution_id = None
        self._institution_name = None

    @property
    def consult_mode(self):
        return self._consult_mode

    @consult_mode.setter
    def consult_mode(self, value):
        self._consult_mode = value
    @property
    def effective(self):
        return self._effective

    @effective.setter
    def effective(self, value):
        self._effective = value
    @property
    def effective_end_date(self):
        return self._effective_end_date

    @effective_end_date.setter
    def effective_end_date(self, value):
        self._effective_end_date = value
    @property
    def effective_start_date(self):
        return self._effective_start_date

    @effective_start_date.setter
    def effective_start_date(self, value):
        self._effective_start_date = value
    @property
    def institution_desc(self):
        return self._institution_desc

    @institution_desc.setter
    def institution_desc(self, value):
        self._institution_desc = value
    @property
    def institution_id(self):
        return self._institution_id

    @institution_id.setter
    def institution_id(self, value):
        self._institution_id = value
    @property
    def institution_name(self):
        return self._institution_name

    @institution_name.setter
    def institution_name(self, value):
        self._institution_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.consult_mode:
            if hasattr(self.consult_mode, 'to_alipay_dict'):
                params['consult_mode'] = self.consult_mode.to_alipay_dict()
            else:
                params['consult_mode'] = self.consult_mode
        if self.effective:
            if hasattr(self.effective, 'to_alipay_dict'):
                params['effective'] = self.effective.to_alipay_dict()
            else:
                params['effective'] = self.effective
        if self.effective_end_date:
            if hasattr(self.effective_end_date, 'to_alipay_dict'):
                params['effective_end_date'] = self.effective_end_date.to_alipay_dict()
            else:
                params['effective_end_date'] = self.effective_end_date
        if self.effective_start_date:
            if hasattr(self.effective_start_date, 'to_alipay_dict'):
                params['effective_start_date'] = self.effective_start_date.to_alipay_dict()
            else:
                params['effective_start_date'] = self.effective_start_date
        if self.institution_desc:
            if hasattr(self.institution_desc, 'to_alipay_dict'):
                params['institution_desc'] = self.institution_desc.to_alipay_dict()
            else:
                params['institution_desc'] = self.institution_desc
        if self.institution_id:
            if hasattr(self.institution_id, 'to_alipay_dict'):
                params['institution_id'] = self.institution_id.to_alipay_dict()
            else:
                params['institution_id'] = self.institution_id
        if self.institution_name:
            if hasattr(self.institution_name, 'to_alipay_dict'):
                params['institution_name'] = self.institution_name.to_alipay_dict()
            else:
                params['institution_name'] = self.institution_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InstitutionBasicInfo()
        if 'consult_mode' in d:
            o.consult_mode = d['consult_mode']
        if 'effective' in d:
            o.effective = d['effective']
        if 'effective_end_date' in d:
            o.effective_end_date = d['effective_end_date']
        if 'effective_start_date' in d:
            o.effective_start_date = d['effective_start_date']
        if 'institution_desc' in d:
            o.institution_desc = d['institution_desc']
        if 'institution_id' in d:
            o.institution_id = d['institution_id']
        if 'institution_name' in d:
            o.institution_name = d['institution_name']
        return o



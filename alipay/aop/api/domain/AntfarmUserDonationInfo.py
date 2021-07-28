#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.AntfarmUserDonationRecord import AntfarmUserDonationRecord


class AntfarmUserDonationInfo(object):

    def __init__(self):
        self._donation_record_list = None
        self._donation_target_id = None
        self._donation_target_name = None
        self._project_id = None
        self._project_name = None

    @property
    def donation_record_list(self):
        return self._donation_record_list

    @donation_record_list.setter
    def donation_record_list(self, value):
        if isinstance(value, list):
            self._donation_record_list = list()
            for i in value:
                if isinstance(i, AntfarmUserDonationRecord):
                    self._donation_record_list.append(i)
                else:
                    self._donation_record_list.append(AntfarmUserDonationRecord.from_alipay_dict(i))
    @property
    def donation_target_id(self):
        return self._donation_target_id

    @donation_target_id.setter
    def donation_target_id(self, value):
        self._donation_target_id = value
    @property
    def donation_target_name(self):
        return self._donation_target_name

    @donation_target_name.setter
    def donation_target_name(self, value):
        self._donation_target_name = value
    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value
    @property
    def project_name(self):
        return self._project_name

    @project_name.setter
    def project_name(self, value):
        self._project_name = value


    def to_alipay_dict(self):
        params = dict()
        if self.donation_record_list:
            if isinstance(self.donation_record_list, list):
                for i in range(0, len(self.donation_record_list)):
                    element = self.donation_record_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.donation_record_list[i] = element.to_alipay_dict()
            if hasattr(self.donation_record_list, 'to_alipay_dict'):
                params['donation_record_list'] = self.donation_record_list.to_alipay_dict()
            else:
                params['donation_record_list'] = self.donation_record_list
        if self.donation_target_id:
            if hasattr(self.donation_target_id, 'to_alipay_dict'):
                params['donation_target_id'] = self.donation_target_id.to_alipay_dict()
            else:
                params['donation_target_id'] = self.donation_target_id
        if self.donation_target_name:
            if hasattr(self.donation_target_name, 'to_alipay_dict'):
                params['donation_target_name'] = self.donation_target_name.to_alipay_dict()
            else:
                params['donation_target_name'] = self.donation_target_name
        if self.project_id:
            if hasattr(self.project_id, 'to_alipay_dict'):
                params['project_id'] = self.project_id.to_alipay_dict()
            else:
                params['project_id'] = self.project_id
        if self.project_name:
            if hasattr(self.project_name, 'to_alipay_dict'):
                params['project_name'] = self.project_name.to_alipay_dict()
            else:
                params['project_name'] = self.project_name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AntfarmUserDonationInfo()
        if 'donation_record_list' in d:
            o.donation_record_list = d['donation_record_list']
        if 'donation_target_id' in d:
            o.donation_target_id = d['donation_target_id']
        if 'donation_target_name' in d:
            o.donation_target_name = d['donation_target_name']
        if 'project_id' in d:
            o.project_id = d['project_id']
        if 'project_name' in d:
            o.project_name = d['project_name']
        return o



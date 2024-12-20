#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentPayContractInfo(object):

    def __init__(self):
        self._draw_end_month = None
        self._draw_starting_month = None
        self._project_closing_month = None
        self._rent_contract_no = None
        self._rent_house_address = None
        self._rent_pay_end_time = None
        self._rent_pay_start_time = None
        self._rent_project_no = None

    @property
    def draw_end_month(self):
        return self._draw_end_month

    @draw_end_month.setter
    def draw_end_month(self, value):
        self._draw_end_month = value
    @property
    def draw_starting_month(self):
        return self._draw_starting_month

    @draw_starting_month.setter
    def draw_starting_month(self, value):
        self._draw_starting_month = value
    @property
    def project_closing_month(self):
        return self._project_closing_month

    @project_closing_month.setter
    def project_closing_month(self, value):
        self._project_closing_month = value
    @property
    def rent_contract_no(self):
        return self._rent_contract_no

    @rent_contract_no.setter
    def rent_contract_no(self, value):
        self._rent_contract_no = value
    @property
    def rent_house_address(self):
        return self._rent_house_address

    @rent_house_address.setter
    def rent_house_address(self, value):
        self._rent_house_address = value
    @property
    def rent_pay_end_time(self):
        return self._rent_pay_end_time

    @rent_pay_end_time.setter
    def rent_pay_end_time(self, value):
        self._rent_pay_end_time = value
    @property
    def rent_pay_start_time(self):
        return self._rent_pay_start_time

    @rent_pay_start_time.setter
    def rent_pay_start_time(self, value):
        self._rent_pay_start_time = value
    @property
    def rent_project_no(self):
        return self._rent_project_no

    @rent_project_no.setter
    def rent_project_no(self, value):
        self._rent_project_no = value


    def to_alipay_dict(self):
        params = dict()
        if self.draw_end_month:
            if hasattr(self.draw_end_month, 'to_alipay_dict'):
                params['draw_end_month'] = self.draw_end_month.to_alipay_dict()
            else:
                params['draw_end_month'] = self.draw_end_month
        if self.draw_starting_month:
            if hasattr(self.draw_starting_month, 'to_alipay_dict'):
                params['draw_starting_month'] = self.draw_starting_month.to_alipay_dict()
            else:
                params['draw_starting_month'] = self.draw_starting_month
        if self.project_closing_month:
            if hasattr(self.project_closing_month, 'to_alipay_dict'):
                params['project_closing_month'] = self.project_closing_month.to_alipay_dict()
            else:
                params['project_closing_month'] = self.project_closing_month
        if self.rent_contract_no:
            if hasattr(self.rent_contract_no, 'to_alipay_dict'):
                params['rent_contract_no'] = self.rent_contract_no.to_alipay_dict()
            else:
                params['rent_contract_no'] = self.rent_contract_no
        if self.rent_house_address:
            if hasattr(self.rent_house_address, 'to_alipay_dict'):
                params['rent_house_address'] = self.rent_house_address.to_alipay_dict()
            else:
                params['rent_house_address'] = self.rent_house_address
        if self.rent_pay_end_time:
            if hasattr(self.rent_pay_end_time, 'to_alipay_dict'):
                params['rent_pay_end_time'] = self.rent_pay_end_time.to_alipay_dict()
            else:
                params['rent_pay_end_time'] = self.rent_pay_end_time
        if self.rent_pay_start_time:
            if hasattr(self.rent_pay_start_time, 'to_alipay_dict'):
                params['rent_pay_start_time'] = self.rent_pay_start_time.to_alipay_dict()
            else:
                params['rent_pay_start_time'] = self.rent_pay_start_time
        if self.rent_project_no:
            if hasattr(self.rent_project_no, 'to_alipay_dict'):
                params['rent_project_no'] = self.rent_project_no.to_alipay_dict()
            else:
                params['rent_project_no'] = self.rent_project_no
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentPayContractInfo()
        if 'draw_end_month' in d:
            o.draw_end_month = d['draw_end_month']
        if 'draw_starting_month' in d:
            o.draw_starting_month = d['draw_starting_month']
        if 'project_closing_month' in d:
            o.project_closing_month = d['project_closing_month']
        if 'rent_contract_no' in d:
            o.rent_contract_no = d['rent_contract_no']
        if 'rent_house_address' in d:
            o.rent_house_address = d['rent_house_address']
        if 'rent_pay_end_time' in d:
            o.rent_pay_end_time = d['rent_pay_end_time']
        if 'rent_pay_start_time' in d:
            o.rent_pay_start_time = d['rent_pay_start_time']
        if 'rent_project_no' in d:
            o.rent_project_no = d['rent_project_no']
        return o



#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ZmepAnnualReportBasicInfo(object):

    def __init__(self):
        self._address = None
        self._control_composition = None
        self._email_address = None
        self._employee_account = None
        self._ep_cert_no = None
        self._ep_name = None
        self._ep_status = None
        self._has_external_guarantee = None
        self._has_external_invest = None
        self._has_shareholder_equity_transfer = None
        self._has_website = None
        self._phone_number = None
        self._postcode = None

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def control_composition(self):
        return self._control_composition

    @control_composition.setter
    def control_composition(self, value):
        self._control_composition = value
    @property
    def email_address(self):
        return self._email_address

    @email_address.setter
    def email_address(self, value):
        self._email_address = value
    @property
    def employee_account(self):
        return self._employee_account

    @employee_account.setter
    def employee_account(self, value):
        self._employee_account = value
    @property
    def ep_cert_no(self):
        return self._ep_cert_no

    @ep_cert_no.setter
    def ep_cert_no(self, value):
        self._ep_cert_no = value
    @property
    def ep_name(self):
        return self._ep_name

    @ep_name.setter
    def ep_name(self, value):
        self._ep_name = value
    @property
    def ep_status(self):
        return self._ep_status

    @ep_status.setter
    def ep_status(self, value):
        self._ep_status = value
    @property
    def has_external_guarantee(self):
        return self._has_external_guarantee

    @has_external_guarantee.setter
    def has_external_guarantee(self, value):
        self._has_external_guarantee = value
    @property
    def has_external_invest(self):
        return self._has_external_invest

    @has_external_invest.setter
    def has_external_invest(self, value):
        self._has_external_invest = value
    @property
    def has_shareholder_equity_transfer(self):
        return self._has_shareholder_equity_transfer

    @has_shareholder_equity_transfer.setter
    def has_shareholder_equity_transfer(self, value):
        self._has_shareholder_equity_transfer = value
    @property
    def has_website(self):
        return self._has_website

    @has_website.setter
    def has_website(self, value):
        self._has_website = value
    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value
    @property
    def postcode(self):
        return self._postcode

    @postcode.setter
    def postcode(self, value):
        self._postcode = value


    def to_alipay_dict(self):
        params = dict()
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.control_composition:
            if hasattr(self.control_composition, 'to_alipay_dict'):
                params['control_composition'] = self.control_composition.to_alipay_dict()
            else:
                params['control_composition'] = self.control_composition
        if self.email_address:
            if hasattr(self.email_address, 'to_alipay_dict'):
                params['email_address'] = self.email_address.to_alipay_dict()
            else:
                params['email_address'] = self.email_address
        if self.employee_account:
            if hasattr(self.employee_account, 'to_alipay_dict'):
                params['employee_account'] = self.employee_account.to_alipay_dict()
            else:
                params['employee_account'] = self.employee_account
        if self.ep_cert_no:
            if hasattr(self.ep_cert_no, 'to_alipay_dict'):
                params['ep_cert_no'] = self.ep_cert_no.to_alipay_dict()
            else:
                params['ep_cert_no'] = self.ep_cert_no
        if self.ep_name:
            if hasattr(self.ep_name, 'to_alipay_dict'):
                params['ep_name'] = self.ep_name.to_alipay_dict()
            else:
                params['ep_name'] = self.ep_name
        if self.ep_status:
            if hasattr(self.ep_status, 'to_alipay_dict'):
                params['ep_status'] = self.ep_status.to_alipay_dict()
            else:
                params['ep_status'] = self.ep_status
        if self.has_external_guarantee:
            if hasattr(self.has_external_guarantee, 'to_alipay_dict'):
                params['has_external_guarantee'] = self.has_external_guarantee.to_alipay_dict()
            else:
                params['has_external_guarantee'] = self.has_external_guarantee
        if self.has_external_invest:
            if hasattr(self.has_external_invest, 'to_alipay_dict'):
                params['has_external_invest'] = self.has_external_invest.to_alipay_dict()
            else:
                params['has_external_invest'] = self.has_external_invest
        if self.has_shareholder_equity_transfer:
            if hasattr(self.has_shareholder_equity_transfer, 'to_alipay_dict'):
                params['has_shareholder_equity_transfer'] = self.has_shareholder_equity_transfer.to_alipay_dict()
            else:
                params['has_shareholder_equity_transfer'] = self.has_shareholder_equity_transfer
        if self.has_website:
            if hasattr(self.has_website, 'to_alipay_dict'):
                params['has_website'] = self.has_website.to_alipay_dict()
            else:
                params['has_website'] = self.has_website
        if self.phone_number:
            if hasattr(self.phone_number, 'to_alipay_dict'):
                params['phone_number'] = self.phone_number.to_alipay_dict()
            else:
                params['phone_number'] = self.phone_number
        if self.postcode:
            if hasattr(self.postcode, 'to_alipay_dict'):
                params['postcode'] = self.postcode.to_alipay_dict()
            else:
                params['postcode'] = self.postcode
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ZmepAnnualReportBasicInfo()
        if 'address' in d:
            o.address = d['address']
        if 'control_composition' in d:
            o.control_composition = d['control_composition']
        if 'email_address' in d:
            o.email_address = d['email_address']
        if 'employee_account' in d:
            o.employee_account = d['employee_account']
        if 'ep_cert_no' in d:
            o.ep_cert_no = d['ep_cert_no']
        if 'ep_name' in d:
            o.ep_name = d['ep_name']
        if 'ep_status' in d:
            o.ep_status = d['ep_status']
        if 'has_external_guarantee' in d:
            o.has_external_guarantee = d['has_external_guarantee']
        if 'has_external_invest' in d:
            o.has_external_invest = d['has_external_invest']
        if 'has_shareholder_equity_transfer' in d:
            o.has_shareholder_equity_transfer = d['has_shareholder_equity_transfer']
        if 'has_website' in d:
            o.has_website = d['has_website']
        if 'phone_number' in d:
            o.phone_number = d['phone_number']
        if 'postcode' in d:
            o.postcode = d['postcode']
        return o



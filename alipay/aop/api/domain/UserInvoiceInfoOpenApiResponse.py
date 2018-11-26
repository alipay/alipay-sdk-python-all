#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.UserMailInfoVO import UserMailInfoVO


class UserInvoiceInfoOpenApiResponse(object):

    def __init__(self):
        self._accept_electronic = None
        self._address = None
        self._auto = None
        self._bank_account = None
        self._bank_name = None
        self._business_licence_url = None
        self._creator = None
        self._gmt_create = None
        self._gmt_modified = None
        self._hold = None
        self._id = None
        self._ip_id = None
        self._last_modifier = None
        self._open_account_permit_url = None
        self._other_qualification_url = None
        self._status = None
        self._task_date = None
        self._tax_no = None
        self._tax_payer_qualification = None
        self._tax_qualification_url = None
        self._tax_reg_cert_url = None
        self._taxpayer_quali_valid = None
        self._telephone = None
        self._title = None
        self._tnt_inst_id = None
        self._type = None
        self._user_mail_info_list = None

    @property
    def accept_electronic(self):
        return self._accept_electronic

    @accept_electronic.setter
    def accept_electronic(self, value):
        self._accept_electronic = value
    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
    @property
    def auto(self):
        return self._auto

    @auto.setter
    def auto(self, value):
        self._auto = value
    @property
    def bank_account(self):
        return self._bank_account

    @bank_account.setter
    def bank_account(self, value):
        self._bank_account = value
    @property
    def bank_name(self):
        return self._bank_name

    @bank_name.setter
    def bank_name(self, value):
        self._bank_name = value
    @property
    def business_licence_url(self):
        return self._business_licence_url

    @business_licence_url.setter
    def business_licence_url(self, value):
        self._business_licence_url = value
    @property
    def creator(self):
        return self._creator

    @creator.setter
    def creator(self, value):
        self._creator = value
    @property
    def gmt_create(self):
        return self._gmt_create

    @gmt_create.setter
    def gmt_create(self, value):
        self._gmt_create = value
    @property
    def gmt_modified(self):
        return self._gmt_modified

    @gmt_modified.setter
    def gmt_modified(self, value):
        self._gmt_modified = value
    @property
    def hold(self):
        return self._hold

    @hold.setter
    def hold(self, value):
        self._hold = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def ip_id(self):
        return self._ip_id

    @ip_id.setter
    def ip_id(self, value):
        self._ip_id = value
    @property
    def last_modifier(self):
        return self._last_modifier

    @last_modifier.setter
    def last_modifier(self, value):
        self._last_modifier = value
    @property
    def open_account_permit_url(self):
        return self._open_account_permit_url

    @open_account_permit_url.setter
    def open_account_permit_url(self, value):
        self._open_account_permit_url = value
    @property
    def other_qualification_url(self):
        return self._other_qualification_url

    @other_qualification_url.setter
    def other_qualification_url(self, value):
        self._other_qualification_url = value
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value
    @property
    def task_date(self):
        return self._task_date

    @task_date.setter
    def task_date(self, value):
        self._task_date = value
    @property
    def tax_no(self):
        return self._tax_no

    @tax_no.setter
    def tax_no(self, value):
        self._tax_no = value
    @property
    def tax_payer_qualification(self):
        return self._tax_payer_qualification

    @tax_payer_qualification.setter
    def tax_payer_qualification(self, value):
        self._tax_payer_qualification = value
    @property
    def tax_qualification_url(self):
        return self._tax_qualification_url

    @tax_qualification_url.setter
    def tax_qualification_url(self, value):
        self._tax_qualification_url = value
    @property
    def tax_reg_cert_url(self):
        return self._tax_reg_cert_url

    @tax_reg_cert_url.setter
    def tax_reg_cert_url(self, value):
        self._tax_reg_cert_url = value
    @property
    def taxpayer_quali_valid(self):
        return self._taxpayer_quali_valid

    @taxpayer_quali_valid.setter
    def taxpayer_quali_valid(self, value):
        self._taxpayer_quali_valid = value
    @property
    def telephone(self):
        return self._telephone

    @telephone.setter
    def telephone(self, value):
        self._telephone = value
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def tnt_inst_id(self):
        return self._tnt_inst_id

    @tnt_inst_id.setter
    def tnt_inst_id(self, value):
        self._tnt_inst_id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
    @property
    def user_mail_info_list(self):
        return self._user_mail_info_list

    @user_mail_info_list.setter
    def user_mail_info_list(self, value):
        if isinstance(value, list):
            self._user_mail_info_list = list()
            for i in value:
                if isinstance(i, UserMailInfoVO):
                    self._user_mail_info_list.append(i)
                else:
                    self._user_mail_info_list.append(UserMailInfoVO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.accept_electronic:
            if hasattr(self.accept_electronic, 'to_alipay_dict'):
                params['accept_electronic'] = self.accept_electronic.to_alipay_dict()
            else:
                params['accept_electronic'] = self.accept_electronic
        if self.address:
            if hasattr(self.address, 'to_alipay_dict'):
                params['address'] = self.address.to_alipay_dict()
            else:
                params['address'] = self.address
        if self.auto:
            if hasattr(self.auto, 'to_alipay_dict'):
                params['auto'] = self.auto.to_alipay_dict()
            else:
                params['auto'] = self.auto
        if self.bank_account:
            if hasattr(self.bank_account, 'to_alipay_dict'):
                params['bank_account'] = self.bank_account.to_alipay_dict()
            else:
                params['bank_account'] = self.bank_account
        if self.bank_name:
            if hasattr(self.bank_name, 'to_alipay_dict'):
                params['bank_name'] = self.bank_name.to_alipay_dict()
            else:
                params['bank_name'] = self.bank_name
        if self.business_licence_url:
            if hasattr(self.business_licence_url, 'to_alipay_dict'):
                params['business_licence_url'] = self.business_licence_url.to_alipay_dict()
            else:
                params['business_licence_url'] = self.business_licence_url
        if self.creator:
            if hasattr(self.creator, 'to_alipay_dict'):
                params['creator'] = self.creator.to_alipay_dict()
            else:
                params['creator'] = self.creator
        if self.gmt_create:
            if hasattr(self.gmt_create, 'to_alipay_dict'):
                params['gmt_create'] = self.gmt_create.to_alipay_dict()
            else:
                params['gmt_create'] = self.gmt_create
        if self.gmt_modified:
            if hasattr(self.gmt_modified, 'to_alipay_dict'):
                params['gmt_modified'] = self.gmt_modified.to_alipay_dict()
            else:
                params['gmt_modified'] = self.gmt_modified
        if self.hold:
            if hasattr(self.hold, 'to_alipay_dict'):
                params['hold'] = self.hold.to_alipay_dict()
            else:
                params['hold'] = self.hold
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.ip_id:
            if hasattr(self.ip_id, 'to_alipay_dict'):
                params['ip_id'] = self.ip_id.to_alipay_dict()
            else:
                params['ip_id'] = self.ip_id
        if self.last_modifier:
            if hasattr(self.last_modifier, 'to_alipay_dict'):
                params['last_modifier'] = self.last_modifier.to_alipay_dict()
            else:
                params['last_modifier'] = self.last_modifier
        if self.open_account_permit_url:
            if hasattr(self.open_account_permit_url, 'to_alipay_dict'):
                params['open_account_permit_url'] = self.open_account_permit_url.to_alipay_dict()
            else:
                params['open_account_permit_url'] = self.open_account_permit_url
        if self.other_qualification_url:
            if hasattr(self.other_qualification_url, 'to_alipay_dict'):
                params['other_qualification_url'] = self.other_qualification_url.to_alipay_dict()
            else:
                params['other_qualification_url'] = self.other_qualification_url
        if self.status:
            if hasattr(self.status, 'to_alipay_dict'):
                params['status'] = self.status.to_alipay_dict()
            else:
                params['status'] = self.status
        if self.task_date:
            if hasattr(self.task_date, 'to_alipay_dict'):
                params['task_date'] = self.task_date.to_alipay_dict()
            else:
                params['task_date'] = self.task_date
        if self.tax_no:
            if hasattr(self.tax_no, 'to_alipay_dict'):
                params['tax_no'] = self.tax_no.to_alipay_dict()
            else:
                params['tax_no'] = self.tax_no
        if self.tax_payer_qualification:
            if hasattr(self.tax_payer_qualification, 'to_alipay_dict'):
                params['tax_payer_qualification'] = self.tax_payer_qualification.to_alipay_dict()
            else:
                params['tax_payer_qualification'] = self.tax_payer_qualification
        if self.tax_qualification_url:
            if hasattr(self.tax_qualification_url, 'to_alipay_dict'):
                params['tax_qualification_url'] = self.tax_qualification_url.to_alipay_dict()
            else:
                params['tax_qualification_url'] = self.tax_qualification_url
        if self.tax_reg_cert_url:
            if hasattr(self.tax_reg_cert_url, 'to_alipay_dict'):
                params['tax_reg_cert_url'] = self.tax_reg_cert_url.to_alipay_dict()
            else:
                params['tax_reg_cert_url'] = self.tax_reg_cert_url
        if self.taxpayer_quali_valid:
            if hasattr(self.taxpayer_quali_valid, 'to_alipay_dict'):
                params['taxpayer_quali_valid'] = self.taxpayer_quali_valid.to_alipay_dict()
            else:
                params['taxpayer_quali_valid'] = self.taxpayer_quali_valid
        if self.telephone:
            if hasattr(self.telephone, 'to_alipay_dict'):
                params['telephone'] = self.telephone.to_alipay_dict()
            else:
                params['telephone'] = self.telephone
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.tnt_inst_id:
            if hasattr(self.tnt_inst_id, 'to_alipay_dict'):
                params['tnt_inst_id'] = self.tnt_inst_id.to_alipay_dict()
            else:
                params['tnt_inst_id'] = self.tnt_inst_id
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        if self.user_mail_info_list:
            if isinstance(self.user_mail_info_list, list):
                for i in range(0, len(self.user_mail_info_list)):
                    element = self.user_mail_info_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.user_mail_info_list[i] = element.to_alipay_dict()
            if hasattr(self.user_mail_info_list, 'to_alipay_dict'):
                params['user_mail_info_list'] = self.user_mail_info_list.to_alipay_dict()
            else:
                params['user_mail_info_list'] = self.user_mail_info_list
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = UserInvoiceInfoOpenApiResponse()
        if 'accept_electronic' in d:
            o.accept_electronic = d['accept_electronic']
        if 'address' in d:
            o.address = d['address']
        if 'auto' in d:
            o.auto = d['auto']
        if 'bank_account' in d:
            o.bank_account = d['bank_account']
        if 'bank_name' in d:
            o.bank_name = d['bank_name']
        if 'business_licence_url' in d:
            o.business_licence_url = d['business_licence_url']
        if 'creator' in d:
            o.creator = d['creator']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'hold' in d:
            o.hold = d['hold']
        if 'id' in d:
            o.id = d['id']
        if 'ip_id' in d:
            o.ip_id = d['ip_id']
        if 'last_modifier' in d:
            o.last_modifier = d['last_modifier']
        if 'open_account_permit_url' in d:
            o.open_account_permit_url = d['open_account_permit_url']
        if 'other_qualification_url' in d:
            o.other_qualification_url = d['other_qualification_url']
        if 'status' in d:
            o.status = d['status']
        if 'task_date' in d:
            o.task_date = d['task_date']
        if 'tax_no' in d:
            o.tax_no = d['tax_no']
        if 'tax_payer_qualification' in d:
            o.tax_payer_qualification = d['tax_payer_qualification']
        if 'tax_qualification_url' in d:
            o.tax_qualification_url = d['tax_qualification_url']
        if 'tax_reg_cert_url' in d:
            o.tax_reg_cert_url = d['tax_reg_cert_url']
        if 'taxpayer_quali_valid' in d:
            o.taxpayer_quali_valid = d['taxpayer_quali_valid']
        if 'telephone' in d:
            o.telephone = d['telephone']
        if 'title' in d:
            o.title = d['title']
        if 'tnt_inst_id' in d:
            o.tnt_inst_id = d['tnt_inst_id']
        if 'type' in d:
            o.type = d['type']
        if 'user_mail_info_list' in d:
            o.user_mail_info_list = d['user_mail_info_list']
        return o



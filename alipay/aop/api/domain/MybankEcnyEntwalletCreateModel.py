#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.UserBaseInfo import UserBaseInfo
from alipay.aop.api.domain.UserBaseInfo import UserBaseInfo
from alipay.aop.api.domain.EcnyAddressInfo import EcnyAddressInfo
from alipay.aop.api.domain.UserBaseInfo import UserBaseInfo
from alipay.aop.api.domain.UserBaseInfo import UserBaseInfo
from alipay.aop.api.domain.EcnyAddressInfo import EcnyAddressInfo
from alipay.aop.api.domain.UserBaseInfo import UserBaseInfo
from alipay.aop.api.domain.UserBaseInfo import UserBaseInfo


class MybankEcnyEntwalletCreateModel(object):

    def __init__(self):
        self._act_ctl_info = None
        self._applicant_info = None
        self._beneficiary_address = None
        self._beneficiary_info = None
        self._contact_info = None
        self._ent_biz_addr = None
        self._ent_biz_scope = None
        self._ent_cert_date_invalid = None
        self._ent_cert_date_valid = None
        self._ent_cert_file = None
        self._ent_cert_no = None
        self._ent_cert_type = None
        self._ent_mcc = None
        self._ent_name = None
        self._ent_reg_cap = None
        self._ent_tax_id = None
        self._ent_type = None
        self._ent_type_desc = None
        self._legal_rep_info = None
        self._other_cert_files = None
        self._other_cert_type = None
        self._out_request_no = None
        self._source_channel = None
        self._super_legal_rep_info = None

    @property
    def act_ctl_info(self):
        return self._act_ctl_info

    @act_ctl_info.setter
    def act_ctl_info(self, value):
        if isinstance(value, UserBaseInfo):
            self._act_ctl_info = value
        else:
            self._act_ctl_info = UserBaseInfo.from_alipay_dict(value)
    @property
    def applicant_info(self):
        return self._applicant_info

    @applicant_info.setter
    def applicant_info(self, value):
        if isinstance(value, UserBaseInfo):
            self._applicant_info = value
        else:
            self._applicant_info = UserBaseInfo.from_alipay_dict(value)
    @property
    def beneficiary_address(self):
        return self._beneficiary_address

    @beneficiary_address.setter
    def beneficiary_address(self, value):
        if isinstance(value, EcnyAddressInfo):
            self._beneficiary_address = value
        else:
            self._beneficiary_address = EcnyAddressInfo.from_alipay_dict(value)
    @property
    def beneficiary_info(self):
        return self._beneficiary_info

    @beneficiary_info.setter
    def beneficiary_info(self, value):
        if isinstance(value, UserBaseInfo):
            self._beneficiary_info = value
        else:
            self._beneficiary_info = UserBaseInfo.from_alipay_dict(value)
    @property
    def contact_info(self):
        return self._contact_info

    @contact_info.setter
    def contact_info(self, value):
        if isinstance(value, UserBaseInfo):
            self._contact_info = value
        else:
            self._contact_info = UserBaseInfo.from_alipay_dict(value)
    @property
    def ent_biz_addr(self):
        return self._ent_biz_addr

    @ent_biz_addr.setter
    def ent_biz_addr(self, value):
        if isinstance(value, EcnyAddressInfo):
            self._ent_biz_addr = value
        else:
            self._ent_biz_addr = EcnyAddressInfo.from_alipay_dict(value)
    @property
    def ent_biz_scope(self):
        return self._ent_biz_scope

    @ent_biz_scope.setter
    def ent_biz_scope(self, value):
        self._ent_biz_scope = value
    @property
    def ent_cert_date_invalid(self):
        return self._ent_cert_date_invalid

    @ent_cert_date_invalid.setter
    def ent_cert_date_invalid(self, value):
        self._ent_cert_date_invalid = value
    @property
    def ent_cert_date_valid(self):
        return self._ent_cert_date_valid

    @ent_cert_date_valid.setter
    def ent_cert_date_valid(self, value):
        self._ent_cert_date_valid = value
    @property
    def ent_cert_file(self):
        return self._ent_cert_file

    @ent_cert_file.setter
    def ent_cert_file(self, value):
        self._ent_cert_file = value
    @property
    def ent_cert_no(self):
        return self._ent_cert_no

    @ent_cert_no.setter
    def ent_cert_no(self, value):
        self._ent_cert_no = value
    @property
    def ent_cert_type(self):
        return self._ent_cert_type

    @ent_cert_type.setter
    def ent_cert_type(self, value):
        self._ent_cert_type = value
    @property
    def ent_mcc(self):
        return self._ent_mcc

    @ent_mcc.setter
    def ent_mcc(self, value):
        self._ent_mcc = value
    @property
    def ent_name(self):
        return self._ent_name

    @ent_name.setter
    def ent_name(self, value):
        self._ent_name = value
    @property
    def ent_reg_cap(self):
        return self._ent_reg_cap

    @ent_reg_cap.setter
    def ent_reg_cap(self, value):
        self._ent_reg_cap = value
    @property
    def ent_tax_id(self):
        return self._ent_tax_id

    @ent_tax_id.setter
    def ent_tax_id(self, value):
        self._ent_tax_id = value
    @property
    def ent_type(self):
        return self._ent_type

    @ent_type.setter
    def ent_type(self, value):
        self._ent_type = value
    @property
    def ent_type_desc(self):
        return self._ent_type_desc

    @ent_type_desc.setter
    def ent_type_desc(self, value):
        self._ent_type_desc = value
    @property
    def legal_rep_info(self):
        return self._legal_rep_info

    @legal_rep_info.setter
    def legal_rep_info(self, value):
        if isinstance(value, UserBaseInfo):
            self._legal_rep_info = value
        else:
            self._legal_rep_info = UserBaseInfo.from_alipay_dict(value)
    @property
    def other_cert_files(self):
        return self._other_cert_files

    @other_cert_files.setter
    def other_cert_files(self, value):
        if isinstance(value, list):
            self._other_cert_files = list()
            for i in value:
                self._other_cert_files.append(i)
    @property
    def other_cert_type(self):
        return self._other_cert_type

    @other_cert_type.setter
    def other_cert_type(self, value):
        self._other_cert_type = value
    @property
    def out_request_no(self):
        return self._out_request_no

    @out_request_no.setter
    def out_request_no(self, value):
        self._out_request_no = value
    @property
    def source_channel(self):
        return self._source_channel

    @source_channel.setter
    def source_channel(self, value):
        self._source_channel = value
    @property
    def super_legal_rep_info(self):
        return self._super_legal_rep_info

    @super_legal_rep_info.setter
    def super_legal_rep_info(self, value):
        if isinstance(value, UserBaseInfo):
            self._super_legal_rep_info = value
        else:
            self._super_legal_rep_info = UserBaseInfo.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.act_ctl_info:
            if hasattr(self.act_ctl_info, 'to_alipay_dict'):
                params['act_ctl_info'] = self.act_ctl_info.to_alipay_dict()
            else:
                params['act_ctl_info'] = self.act_ctl_info
        if self.applicant_info:
            if hasattr(self.applicant_info, 'to_alipay_dict'):
                params['applicant_info'] = self.applicant_info.to_alipay_dict()
            else:
                params['applicant_info'] = self.applicant_info
        if self.beneficiary_address:
            if hasattr(self.beneficiary_address, 'to_alipay_dict'):
                params['beneficiary_address'] = self.beneficiary_address.to_alipay_dict()
            else:
                params['beneficiary_address'] = self.beneficiary_address
        if self.beneficiary_info:
            if hasattr(self.beneficiary_info, 'to_alipay_dict'):
                params['beneficiary_info'] = self.beneficiary_info.to_alipay_dict()
            else:
                params['beneficiary_info'] = self.beneficiary_info
        if self.contact_info:
            if hasattr(self.contact_info, 'to_alipay_dict'):
                params['contact_info'] = self.contact_info.to_alipay_dict()
            else:
                params['contact_info'] = self.contact_info
        if self.ent_biz_addr:
            if hasattr(self.ent_biz_addr, 'to_alipay_dict'):
                params['ent_biz_addr'] = self.ent_biz_addr.to_alipay_dict()
            else:
                params['ent_biz_addr'] = self.ent_biz_addr
        if self.ent_biz_scope:
            if hasattr(self.ent_biz_scope, 'to_alipay_dict'):
                params['ent_biz_scope'] = self.ent_biz_scope.to_alipay_dict()
            else:
                params['ent_biz_scope'] = self.ent_biz_scope
        if self.ent_cert_date_invalid:
            if hasattr(self.ent_cert_date_invalid, 'to_alipay_dict'):
                params['ent_cert_date_invalid'] = self.ent_cert_date_invalid.to_alipay_dict()
            else:
                params['ent_cert_date_invalid'] = self.ent_cert_date_invalid
        if self.ent_cert_date_valid:
            if hasattr(self.ent_cert_date_valid, 'to_alipay_dict'):
                params['ent_cert_date_valid'] = self.ent_cert_date_valid.to_alipay_dict()
            else:
                params['ent_cert_date_valid'] = self.ent_cert_date_valid
        if self.ent_cert_file:
            if hasattr(self.ent_cert_file, 'to_alipay_dict'):
                params['ent_cert_file'] = self.ent_cert_file.to_alipay_dict()
            else:
                params['ent_cert_file'] = self.ent_cert_file
        if self.ent_cert_no:
            if hasattr(self.ent_cert_no, 'to_alipay_dict'):
                params['ent_cert_no'] = self.ent_cert_no.to_alipay_dict()
            else:
                params['ent_cert_no'] = self.ent_cert_no
        if self.ent_cert_type:
            if hasattr(self.ent_cert_type, 'to_alipay_dict'):
                params['ent_cert_type'] = self.ent_cert_type.to_alipay_dict()
            else:
                params['ent_cert_type'] = self.ent_cert_type
        if self.ent_mcc:
            if hasattr(self.ent_mcc, 'to_alipay_dict'):
                params['ent_mcc'] = self.ent_mcc.to_alipay_dict()
            else:
                params['ent_mcc'] = self.ent_mcc
        if self.ent_name:
            if hasattr(self.ent_name, 'to_alipay_dict'):
                params['ent_name'] = self.ent_name.to_alipay_dict()
            else:
                params['ent_name'] = self.ent_name
        if self.ent_reg_cap:
            if hasattr(self.ent_reg_cap, 'to_alipay_dict'):
                params['ent_reg_cap'] = self.ent_reg_cap.to_alipay_dict()
            else:
                params['ent_reg_cap'] = self.ent_reg_cap
        if self.ent_tax_id:
            if hasattr(self.ent_tax_id, 'to_alipay_dict'):
                params['ent_tax_id'] = self.ent_tax_id.to_alipay_dict()
            else:
                params['ent_tax_id'] = self.ent_tax_id
        if self.ent_type:
            if hasattr(self.ent_type, 'to_alipay_dict'):
                params['ent_type'] = self.ent_type.to_alipay_dict()
            else:
                params['ent_type'] = self.ent_type
        if self.ent_type_desc:
            if hasattr(self.ent_type_desc, 'to_alipay_dict'):
                params['ent_type_desc'] = self.ent_type_desc.to_alipay_dict()
            else:
                params['ent_type_desc'] = self.ent_type_desc
        if self.legal_rep_info:
            if hasattr(self.legal_rep_info, 'to_alipay_dict'):
                params['legal_rep_info'] = self.legal_rep_info.to_alipay_dict()
            else:
                params['legal_rep_info'] = self.legal_rep_info
        if self.other_cert_files:
            if isinstance(self.other_cert_files, list):
                for i in range(0, len(self.other_cert_files)):
                    element = self.other_cert_files[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.other_cert_files[i] = element.to_alipay_dict()
            if hasattr(self.other_cert_files, 'to_alipay_dict'):
                params['other_cert_files'] = self.other_cert_files.to_alipay_dict()
            else:
                params['other_cert_files'] = self.other_cert_files
        if self.other_cert_type:
            if hasattr(self.other_cert_type, 'to_alipay_dict'):
                params['other_cert_type'] = self.other_cert_type.to_alipay_dict()
            else:
                params['other_cert_type'] = self.other_cert_type
        if self.out_request_no:
            if hasattr(self.out_request_no, 'to_alipay_dict'):
                params['out_request_no'] = self.out_request_no.to_alipay_dict()
            else:
                params['out_request_no'] = self.out_request_no
        if self.source_channel:
            if hasattr(self.source_channel, 'to_alipay_dict'):
                params['source_channel'] = self.source_channel.to_alipay_dict()
            else:
                params['source_channel'] = self.source_channel
        if self.super_legal_rep_info:
            if hasattr(self.super_legal_rep_info, 'to_alipay_dict'):
                params['super_legal_rep_info'] = self.super_legal_rep_info.to_alipay_dict()
            else:
                params['super_legal_rep_info'] = self.super_legal_rep_info
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankEcnyEntwalletCreateModel()
        if 'act_ctl_info' in d:
            o.act_ctl_info = d['act_ctl_info']
        if 'applicant_info' in d:
            o.applicant_info = d['applicant_info']
        if 'beneficiary_address' in d:
            o.beneficiary_address = d['beneficiary_address']
        if 'beneficiary_info' in d:
            o.beneficiary_info = d['beneficiary_info']
        if 'contact_info' in d:
            o.contact_info = d['contact_info']
        if 'ent_biz_addr' in d:
            o.ent_biz_addr = d['ent_biz_addr']
        if 'ent_biz_scope' in d:
            o.ent_biz_scope = d['ent_biz_scope']
        if 'ent_cert_date_invalid' in d:
            o.ent_cert_date_invalid = d['ent_cert_date_invalid']
        if 'ent_cert_date_valid' in d:
            o.ent_cert_date_valid = d['ent_cert_date_valid']
        if 'ent_cert_file' in d:
            o.ent_cert_file = d['ent_cert_file']
        if 'ent_cert_no' in d:
            o.ent_cert_no = d['ent_cert_no']
        if 'ent_cert_type' in d:
            o.ent_cert_type = d['ent_cert_type']
        if 'ent_mcc' in d:
            o.ent_mcc = d['ent_mcc']
        if 'ent_name' in d:
            o.ent_name = d['ent_name']
        if 'ent_reg_cap' in d:
            o.ent_reg_cap = d['ent_reg_cap']
        if 'ent_tax_id' in d:
            o.ent_tax_id = d['ent_tax_id']
        if 'ent_type' in d:
            o.ent_type = d['ent_type']
        if 'ent_type_desc' in d:
            o.ent_type_desc = d['ent_type_desc']
        if 'legal_rep_info' in d:
            o.legal_rep_info = d['legal_rep_info']
        if 'other_cert_files' in d:
            o.other_cert_files = d['other_cert_files']
        if 'other_cert_type' in d:
            o.other_cert_type = d['other_cert_type']
        if 'out_request_no' in d:
            o.out_request_no = d['out_request_no']
        if 'source_channel' in d:
            o.source_channel = d['source_channel']
        if 'super_legal_rep_info' in d:
            o.super_legal_rep_info = d['super_legal_rep_info']
        return o



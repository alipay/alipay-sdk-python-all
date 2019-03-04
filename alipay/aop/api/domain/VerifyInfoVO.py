#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LegalRepresentativeVO import LegalRepresentativeVO
from alipay.aop.api.domain.ManagerVO import ManagerVO
from alipay.aop.api.domain.StockHolderVO import StockHolderVO
from alipay.aop.api.domain.UboVO import UboVO


class VerifyInfoVO(object):

    def __init__(self):
        self._business_address = None
        self._company_name = None
        self._ever_org_name = None
        self._industry_name = None
        self._legal_representative = None
        self._local_tax_no = None
        self._logoff_date = None
        self._managers = None
        self._norm_opr_project = None
        self._opr_status = None
        self._oprt_end_date = None
        self._oprt_start_date = None
        self._org_actual_cptl = None
        self._org_reg_addr = None
        self._org_reg_cptl = None
        self._org_reg_cptl_curcy = None
        self._org_reg_opr_scope = None
        self._org_type = None
        self._org_website = None
        self._permit_opr_project = None
        self._registration_country = None
        self._registration_date = None
        self._registration_no = None
        self._revoke_date = None
        self._stock_holders = None
        self._ubos = None
        self._uc_code = None

    @property
    def business_address(self):
        return self._business_address

    @business_address.setter
    def business_address(self, value):
        self._business_address = value
    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
    @property
    def ever_org_name(self):
        return self._ever_org_name

    @ever_org_name.setter
    def ever_org_name(self, value):
        self._ever_org_name = value
    @property
    def industry_name(self):
        return self._industry_name

    @industry_name.setter
    def industry_name(self, value):
        self._industry_name = value
    @property
    def legal_representative(self):
        return self._legal_representative

    @legal_representative.setter
    def legal_representative(self, value):
        if isinstance(value, LegalRepresentativeVO):
            self._legal_representative = value
        else:
            self._legal_representative = LegalRepresentativeVO.from_alipay_dict(value)
    @property
    def local_tax_no(self):
        return self._local_tax_no

    @local_tax_no.setter
    def local_tax_no(self, value):
        self._local_tax_no = value
    @property
    def logoff_date(self):
        return self._logoff_date

    @logoff_date.setter
    def logoff_date(self, value):
        self._logoff_date = value
    @property
    def managers(self):
        return self._managers

    @managers.setter
    def managers(self, value):
        if isinstance(value, list):
            self._managers = list()
            for i in value:
                if isinstance(i, ManagerVO):
                    self._managers.append(i)
                else:
                    self._managers.append(ManagerVO.from_alipay_dict(i))
    @property
    def norm_opr_project(self):
        return self._norm_opr_project

    @norm_opr_project.setter
    def norm_opr_project(self, value):
        self._norm_opr_project = value
    @property
    def opr_status(self):
        return self._opr_status

    @opr_status.setter
    def opr_status(self, value):
        self._opr_status = value
    @property
    def oprt_end_date(self):
        return self._oprt_end_date

    @oprt_end_date.setter
    def oprt_end_date(self, value):
        self._oprt_end_date = value
    @property
    def oprt_start_date(self):
        return self._oprt_start_date

    @oprt_start_date.setter
    def oprt_start_date(self, value):
        self._oprt_start_date = value
    @property
    def org_actual_cptl(self):
        return self._org_actual_cptl

    @org_actual_cptl.setter
    def org_actual_cptl(self, value):
        self._org_actual_cptl = value
    @property
    def org_reg_addr(self):
        return self._org_reg_addr

    @org_reg_addr.setter
    def org_reg_addr(self, value):
        self._org_reg_addr = value
    @property
    def org_reg_cptl(self):
        return self._org_reg_cptl

    @org_reg_cptl.setter
    def org_reg_cptl(self, value):
        self._org_reg_cptl = value
    @property
    def org_reg_cptl_curcy(self):
        return self._org_reg_cptl_curcy

    @org_reg_cptl_curcy.setter
    def org_reg_cptl_curcy(self, value):
        self._org_reg_cptl_curcy = value
    @property
    def org_reg_opr_scope(self):
        return self._org_reg_opr_scope

    @org_reg_opr_scope.setter
    def org_reg_opr_scope(self, value):
        self._org_reg_opr_scope = value
    @property
    def org_type(self):
        return self._org_type

    @org_type.setter
    def org_type(self, value):
        self._org_type = value
    @property
    def org_website(self):
        return self._org_website

    @org_website.setter
    def org_website(self, value):
        self._org_website = value
    @property
    def permit_opr_project(self):
        return self._permit_opr_project

    @permit_opr_project.setter
    def permit_opr_project(self, value):
        self._permit_opr_project = value
    @property
    def registration_country(self):
        return self._registration_country

    @registration_country.setter
    def registration_country(self, value):
        self._registration_country = value
    @property
    def registration_date(self):
        return self._registration_date

    @registration_date.setter
    def registration_date(self, value):
        self._registration_date = value
    @property
    def registration_no(self):
        return self._registration_no

    @registration_no.setter
    def registration_no(self, value):
        self._registration_no = value
    @property
    def revoke_date(self):
        return self._revoke_date

    @revoke_date.setter
    def revoke_date(self, value):
        self._revoke_date = value
    @property
    def stock_holders(self):
        return self._stock_holders

    @stock_holders.setter
    def stock_holders(self, value):
        if isinstance(value, list):
            self._stock_holders = list()
            for i in value:
                if isinstance(i, StockHolderVO):
                    self._stock_holders.append(i)
                else:
                    self._stock_holders.append(StockHolderVO.from_alipay_dict(i))
    @property
    def ubos(self):
        return self._ubos

    @ubos.setter
    def ubos(self, value):
        if isinstance(value, list):
            self._ubos = list()
            for i in value:
                if isinstance(i, UboVO):
                    self._ubos.append(i)
                else:
                    self._ubos.append(UboVO.from_alipay_dict(i))
    @property
    def uc_code(self):
        return self._uc_code

    @uc_code.setter
    def uc_code(self, value):
        self._uc_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.business_address:
            if hasattr(self.business_address, 'to_alipay_dict'):
                params['business_address'] = self.business_address.to_alipay_dict()
            else:
                params['business_address'] = self.business_address
        if self.company_name:
            if hasattr(self.company_name, 'to_alipay_dict'):
                params['company_name'] = self.company_name.to_alipay_dict()
            else:
                params['company_name'] = self.company_name
        if self.ever_org_name:
            if hasattr(self.ever_org_name, 'to_alipay_dict'):
                params['ever_org_name'] = self.ever_org_name.to_alipay_dict()
            else:
                params['ever_org_name'] = self.ever_org_name
        if self.industry_name:
            if hasattr(self.industry_name, 'to_alipay_dict'):
                params['industry_name'] = self.industry_name.to_alipay_dict()
            else:
                params['industry_name'] = self.industry_name
        if self.legal_representative:
            if hasattr(self.legal_representative, 'to_alipay_dict'):
                params['legal_representative'] = self.legal_representative.to_alipay_dict()
            else:
                params['legal_representative'] = self.legal_representative
        if self.local_tax_no:
            if hasattr(self.local_tax_no, 'to_alipay_dict'):
                params['local_tax_no'] = self.local_tax_no.to_alipay_dict()
            else:
                params['local_tax_no'] = self.local_tax_no
        if self.logoff_date:
            if hasattr(self.logoff_date, 'to_alipay_dict'):
                params['logoff_date'] = self.logoff_date.to_alipay_dict()
            else:
                params['logoff_date'] = self.logoff_date
        if self.managers:
            if isinstance(self.managers, list):
                for i in range(0, len(self.managers)):
                    element = self.managers[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.managers[i] = element.to_alipay_dict()
            if hasattr(self.managers, 'to_alipay_dict'):
                params['managers'] = self.managers.to_alipay_dict()
            else:
                params['managers'] = self.managers
        if self.norm_opr_project:
            if hasattr(self.norm_opr_project, 'to_alipay_dict'):
                params['norm_opr_project'] = self.norm_opr_project.to_alipay_dict()
            else:
                params['norm_opr_project'] = self.norm_opr_project
        if self.opr_status:
            if hasattr(self.opr_status, 'to_alipay_dict'):
                params['opr_status'] = self.opr_status.to_alipay_dict()
            else:
                params['opr_status'] = self.opr_status
        if self.oprt_end_date:
            if hasattr(self.oprt_end_date, 'to_alipay_dict'):
                params['oprt_end_date'] = self.oprt_end_date.to_alipay_dict()
            else:
                params['oprt_end_date'] = self.oprt_end_date
        if self.oprt_start_date:
            if hasattr(self.oprt_start_date, 'to_alipay_dict'):
                params['oprt_start_date'] = self.oprt_start_date.to_alipay_dict()
            else:
                params['oprt_start_date'] = self.oprt_start_date
        if self.org_actual_cptl:
            if hasattr(self.org_actual_cptl, 'to_alipay_dict'):
                params['org_actual_cptl'] = self.org_actual_cptl.to_alipay_dict()
            else:
                params['org_actual_cptl'] = self.org_actual_cptl
        if self.org_reg_addr:
            if hasattr(self.org_reg_addr, 'to_alipay_dict'):
                params['org_reg_addr'] = self.org_reg_addr.to_alipay_dict()
            else:
                params['org_reg_addr'] = self.org_reg_addr
        if self.org_reg_cptl:
            if hasattr(self.org_reg_cptl, 'to_alipay_dict'):
                params['org_reg_cptl'] = self.org_reg_cptl.to_alipay_dict()
            else:
                params['org_reg_cptl'] = self.org_reg_cptl
        if self.org_reg_cptl_curcy:
            if hasattr(self.org_reg_cptl_curcy, 'to_alipay_dict'):
                params['org_reg_cptl_curcy'] = self.org_reg_cptl_curcy.to_alipay_dict()
            else:
                params['org_reg_cptl_curcy'] = self.org_reg_cptl_curcy
        if self.org_reg_opr_scope:
            if hasattr(self.org_reg_opr_scope, 'to_alipay_dict'):
                params['org_reg_opr_scope'] = self.org_reg_opr_scope.to_alipay_dict()
            else:
                params['org_reg_opr_scope'] = self.org_reg_opr_scope
        if self.org_type:
            if hasattr(self.org_type, 'to_alipay_dict'):
                params['org_type'] = self.org_type.to_alipay_dict()
            else:
                params['org_type'] = self.org_type
        if self.org_website:
            if hasattr(self.org_website, 'to_alipay_dict'):
                params['org_website'] = self.org_website.to_alipay_dict()
            else:
                params['org_website'] = self.org_website
        if self.permit_opr_project:
            if hasattr(self.permit_opr_project, 'to_alipay_dict'):
                params['permit_opr_project'] = self.permit_opr_project.to_alipay_dict()
            else:
                params['permit_opr_project'] = self.permit_opr_project
        if self.registration_country:
            if hasattr(self.registration_country, 'to_alipay_dict'):
                params['registration_country'] = self.registration_country.to_alipay_dict()
            else:
                params['registration_country'] = self.registration_country
        if self.registration_date:
            if hasattr(self.registration_date, 'to_alipay_dict'):
                params['registration_date'] = self.registration_date.to_alipay_dict()
            else:
                params['registration_date'] = self.registration_date
        if self.registration_no:
            if hasattr(self.registration_no, 'to_alipay_dict'):
                params['registration_no'] = self.registration_no.to_alipay_dict()
            else:
                params['registration_no'] = self.registration_no
        if self.revoke_date:
            if hasattr(self.revoke_date, 'to_alipay_dict'):
                params['revoke_date'] = self.revoke_date.to_alipay_dict()
            else:
                params['revoke_date'] = self.revoke_date
        if self.stock_holders:
            if isinstance(self.stock_holders, list):
                for i in range(0, len(self.stock_holders)):
                    element = self.stock_holders[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.stock_holders[i] = element.to_alipay_dict()
            if hasattr(self.stock_holders, 'to_alipay_dict'):
                params['stock_holders'] = self.stock_holders.to_alipay_dict()
            else:
                params['stock_holders'] = self.stock_holders
        if self.ubos:
            if isinstance(self.ubos, list):
                for i in range(0, len(self.ubos)):
                    element = self.ubos[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ubos[i] = element.to_alipay_dict()
            if hasattr(self.ubos, 'to_alipay_dict'):
                params['ubos'] = self.ubos.to_alipay_dict()
            else:
                params['ubos'] = self.ubos
        if self.uc_code:
            if hasattr(self.uc_code, 'to_alipay_dict'):
                params['uc_code'] = self.uc_code.to_alipay_dict()
            else:
                params['uc_code'] = self.uc_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = VerifyInfoVO()
        if 'business_address' in d:
            o.business_address = d['business_address']
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'ever_org_name' in d:
            o.ever_org_name = d['ever_org_name']
        if 'industry_name' in d:
            o.industry_name = d['industry_name']
        if 'legal_representative' in d:
            o.legal_representative = d['legal_representative']
        if 'local_tax_no' in d:
            o.local_tax_no = d['local_tax_no']
        if 'logoff_date' in d:
            o.logoff_date = d['logoff_date']
        if 'managers' in d:
            o.managers = d['managers']
        if 'norm_opr_project' in d:
            o.norm_opr_project = d['norm_opr_project']
        if 'opr_status' in d:
            o.opr_status = d['opr_status']
        if 'oprt_end_date' in d:
            o.oprt_end_date = d['oprt_end_date']
        if 'oprt_start_date' in d:
            o.oprt_start_date = d['oprt_start_date']
        if 'org_actual_cptl' in d:
            o.org_actual_cptl = d['org_actual_cptl']
        if 'org_reg_addr' in d:
            o.org_reg_addr = d['org_reg_addr']
        if 'org_reg_cptl' in d:
            o.org_reg_cptl = d['org_reg_cptl']
        if 'org_reg_cptl_curcy' in d:
            o.org_reg_cptl_curcy = d['org_reg_cptl_curcy']
        if 'org_reg_opr_scope' in d:
            o.org_reg_opr_scope = d['org_reg_opr_scope']
        if 'org_type' in d:
            o.org_type = d['org_type']
        if 'org_website' in d:
            o.org_website = d['org_website']
        if 'permit_opr_project' in d:
            o.permit_opr_project = d['permit_opr_project']
        if 'registration_country' in d:
            o.registration_country = d['registration_country']
        if 'registration_date' in d:
            o.registration_date = d['registration_date']
        if 'registration_no' in d:
            o.registration_no = d['registration_no']
        if 'revoke_date' in d:
            o.revoke_date = d['revoke_date']
        if 'stock_holders' in d:
            o.stock_holders = d['stock_holders']
        if 'ubos' in d:
            o.ubos = d['ubos']
        if 'uc_code' in d:
            o.uc_code = d['uc_code']
        return o



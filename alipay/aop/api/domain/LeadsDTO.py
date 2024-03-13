#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class LeadsDTO(object):

    def __init__(self):
        self._bd_dept_name = None
        self._bd_name = None
        self._bd_work_no = None
        self._crm_customer_id = None
        self._crm_customer_name = None
        self._deploy_type = None
        self._deploy_type_str = None
        self._gmt_create = None
        self._gmt_modified = None
        self._id = None
        self._lead_id = None
        self._ob_sa_name = None
        self._ob_sa_work_no = None
        self._project_phase = None
        self._project_phase_name = None
        self._sign_probability = None
        self._sign_probability_str = None

    @property
    def bd_dept_name(self):
        return self._bd_dept_name

    @bd_dept_name.setter
    def bd_dept_name(self, value):
        self._bd_dept_name = value
    @property
    def bd_name(self):
        return self._bd_name

    @bd_name.setter
    def bd_name(self, value):
        self._bd_name = value
    @property
    def bd_work_no(self):
        return self._bd_work_no

    @bd_work_no.setter
    def bd_work_no(self, value):
        self._bd_work_no = value
    @property
    def crm_customer_id(self):
        return self._crm_customer_id

    @crm_customer_id.setter
    def crm_customer_id(self, value):
        self._crm_customer_id = value
    @property
    def crm_customer_name(self):
        return self._crm_customer_name

    @crm_customer_name.setter
    def crm_customer_name(self, value):
        self._crm_customer_name = value
    @property
    def deploy_type(self):
        return self._deploy_type

    @deploy_type.setter
    def deploy_type(self, value):
        self._deploy_type = value
    @property
    def deploy_type_str(self):
        return self._deploy_type_str

    @deploy_type_str.setter
    def deploy_type_str(self, value):
        self._deploy_type_str = value
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
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def lead_id(self):
        return self._lead_id

    @lead_id.setter
    def lead_id(self, value):
        self._lead_id = value
    @property
    def ob_sa_name(self):
        return self._ob_sa_name

    @ob_sa_name.setter
    def ob_sa_name(self, value):
        self._ob_sa_name = value
    @property
    def ob_sa_work_no(self):
        return self._ob_sa_work_no

    @ob_sa_work_no.setter
    def ob_sa_work_no(self, value):
        self._ob_sa_work_no = value
    @property
    def project_phase(self):
        return self._project_phase

    @project_phase.setter
    def project_phase(self, value):
        self._project_phase = value
    @property
    def project_phase_name(self):
        return self._project_phase_name

    @project_phase_name.setter
    def project_phase_name(self, value):
        self._project_phase_name = value
    @property
    def sign_probability(self):
        return self._sign_probability

    @sign_probability.setter
    def sign_probability(self, value):
        self._sign_probability = value
    @property
    def sign_probability_str(self):
        return self._sign_probability_str

    @sign_probability_str.setter
    def sign_probability_str(self, value):
        self._sign_probability_str = value


    def to_alipay_dict(self):
        params = dict()
        if self.bd_dept_name:
            if hasattr(self.bd_dept_name, 'to_alipay_dict'):
                params['bd_dept_name'] = self.bd_dept_name.to_alipay_dict()
            else:
                params['bd_dept_name'] = self.bd_dept_name
        if self.bd_name:
            if hasattr(self.bd_name, 'to_alipay_dict'):
                params['bd_name'] = self.bd_name.to_alipay_dict()
            else:
                params['bd_name'] = self.bd_name
        if self.bd_work_no:
            if hasattr(self.bd_work_no, 'to_alipay_dict'):
                params['bd_work_no'] = self.bd_work_no.to_alipay_dict()
            else:
                params['bd_work_no'] = self.bd_work_no
        if self.crm_customer_id:
            if hasattr(self.crm_customer_id, 'to_alipay_dict'):
                params['crm_customer_id'] = self.crm_customer_id.to_alipay_dict()
            else:
                params['crm_customer_id'] = self.crm_customer_id
        if self.crm_customer_name:
            if hasattr(self.crm_customer_name, 'to_alipay_dict'):
                params['crm_customer_name'] = self.crm_customer_name.to_alipay_dict()
            else:
                params['crm_customer_name'] = self.crm_customer_name
        if self.deploy_type:
            if hasattr(self.deploy_type, 'to_alipay_dict'):
                params['deploy_type'] = self.deploy_type.to_alipay_dict()
            else:
                params['deploy_type'] = self.deploy_type
        if self.deploy_type_str:
            if hasattr(self.deploy_type_str, 'to_alipay_dict'):
                params['deploy_type_str'] = self.deploy_type_str.to_alipay_dict()
            else:
                params['deploy_type_str'] = self.deploy_type_str
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
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.lead_id:
            if hasattr(self.lead_id, 'to_alipay_dict'):
                params['lead_id'] = self.lead_id.to_alipay_dict()
            else:
                params['lead_id'] = self.lead_id
        if self.ob_sa_name:
            if hasattr(self.ob_sa_name, 'to_alipay_dict'):
                params['ob_sa_name'] = self.ob_sa_name.to_alipay_dict()
            else:
                params['ob_sa_name'] = self.ob_sa_name
        if self.ob_sa_work_no:
            if hasattr(self.ob_sa_work_no, 'to_alipay_dict'):
                params['ob_sa_work_no'] = self.ob_sa_work_no.to_alipay_dict()
            else:
                params['ob_sa_work_no'] = self.ob_sa_work_no
        if self.project_phase:
            if hasattr(self.project_phase, 'to_alipay_dict'):
                params['project_phase'] = self.project_phase.to_alipay_dict()
            else:
                params['project_phase'] = self.project_phase
        if self.project_phase_name:
            if hasattr(self.project_phase_name, 'to_alipay_dict'):
                params['project_phase_name'] = self.project_phase_name.to_alipay_dict()
            else:
                params['project_phase_name'] = self.project_phase_name
        if self.sign_probability:
            if hasattr(self.sign_probability, 'to_alipay_dict'):
                params['sign_probability'] = self.sign_probability.to_alipay_dict()
            else:
                params['sign_probability'] = self.sign_probability
        if self.sign_probability_str:
            if hasattr(self.sign_probability_str, 'to_alipay_dict'):
                params['sign_probability_str'] = self.sign_probability_str.to_alipay_dict()
            else:
                params['sign_probability_str'] = self.sign_probability_str
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LeadsDTO()
        if 'bd_dept_name' in d:
            o.bd_dept_name = d['bd_dept_name']
        if 'bd_name' in d:
            o.bd_name = d['bd_name']
        if 'bd_work_no' in d:
            o.bd_work_no = d['bd_work_no']
        if 'crm_customer_id' in d:
            o.crm_customer_id = d['crm_customer_id']
        if 'crm_customer_name' in d:
            o.crm_customer_name = d['crm_customer_name']
        if 'deploy_type' in d:
            o.deploy_type = d['deploy_type']
        if 'deploy_type_str' in d:
            o.deploy_type_str = d['deploy_type_str']
        if 'gmt_create' in d:
            o.gmt_create = d['gmt_create']
        if 'gmt_modified' in d:
            o.gmt_modified = d['gmt_modified']
        if 'id' in d:
            o.id = d['id']
        if 'lead_id' in d:
            o.lead_id = d['lead_id']
        if 'ob_sa_name' in d:
            o.ob_sa_name = d['ob_sa_name']
        if 'ob_sa_work_no' in d:
            o.ob_sa_work_no = d['ob_sa_work_no']
        if 'project_phase' in d:
            o.project_phase = d['project_phase']
        if 'project_phase_name' in d:
            o.project_phase_name = d['project_phase_name']
        if 'sign_probability' in d:
            o.sign_probability = d['sign_probability']
        if 'sign_probability_str' in d:
            o.sign_probability_str = d['sign_probability_str']
        return o



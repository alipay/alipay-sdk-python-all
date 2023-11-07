#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FxiaokeCreateOrUpdateLeadsPredictRecordItemRequest import FxiaokeCreateOrUpdateLeadsPredictRecordItemRequest


class FxiaokeCreateLeadsParams(object):

    def __init__(self):
        self._actual_lead_party = None
        self._ali_cloud_bpid_list = None
        self._bid_type = None
        self._cbm_work_no_list = None
        self._cloud_platform_region = None
        self._creator = None
        self._crm_customer_id = None
        self._crm_customer_industry = None
        self._crm_customer_name = None
        self._customer_id = None
        self._deploy_platform = None
        self._deploy_type = None
        self._expect_bid_date = None
        self._expect_sign_date = None
        self._id = None
        self._is_bid = None
        self._is_issue_for_bid = None
        self._leads_code = None
        self._leads_source_partner_id = None
        self._other_partner_pid_list = None
        self._other_party_sign_subject = None
        self._other_party_sign_subject_id = None
        self._our_sign_subject = None
        self._partner_id = None
        self._partner_name = None
        self._predict_clusters_storage_capacity = None
        self._predict_clusters_storage_unit = None
        self._predict_clusters_units_count = None
        self._predict_instance_core_count = None
        self._product_family = None
        self._project_name = None
        self._project_phase = None
        self._record_list = None
        self._related_leads_id = None
        self._resource_foundation = None
        self._sign_path = None
        self._sign_probability = None
        self._software_subscription_years_expand_ten = None
        self._source = None
        self._type = None

    @property
    def actual_lead_party(self):
        return self._actual_lead_party

    @actual_lead_party.setter
    def actual_lead_party(self, value):
        self._actual_lead_party = value
    @property
    def ali_cloud_bpid_list(self):
        return self._ali_cloud_bpid_list

    @ali_cloud_bpid_list.setter
    def ali_cloud_bpid_list(self, value):
        self._ali_cloud_bpid_list = value
    @property
    def bid_type(self):
        return self._bid_type

    @bid_type.setter
    def bid_type(self, value):
        self._bid_type = value
    @property
    def cbm_work_no_list(self):
        return self._cbm_work_no_list

    @cbm_work_no_list.setter
    def cbm_work_no_list(self, value):
        if isinstance(value, list):
            self._cbm_work_no_list = list()
            for i in value:
                self._cbm_work_no_list.append(i)
    @property
    def cloud_platform_region(self):
        return self._cloud_platform_region

    @cloud_platform_region.setter
    def cloud_platform_region(self, value):
        self._cloud_platform_region = value
    @property
    def creator(self):
        return self._creator

    @creator.setter
    def creator(self, value):
        self._creator = value
    @property
    def crm_customer_id(self):
        return self._crm_customer_id

    @crm_customer_id.setter
    def crm_customer_id(self, value):
        self._crm_customer_id = value
    @property
    def crm_customer_industry(self):
        return self._crm_customer_industry

    @crm_customer_industry.setter
    def crm_customer_industry(self, value):
        self._crm_customer_industry = value
    @property
    def crm_customer_name(self):
        return self._crm_customer_name

    @crm_customer_name.setter
    def crm_customer_name(self, value):
        self._crm_customer_name = value
    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value
    @property
    def deploy_platform(self):
        return self._deploy_platform

    @deploy_platform.setter
    def deploy_platform(self, value):
        self._deploy_platform = value
    @property
    def deploy_type(self):
        return self._deploy_type

    @deploy_type.setter
    def deploy_type(self, value):
        self._deploy_type = value
    @property
    def expect_bid_date(self):
        return self._expect_bid_date

    @expect_bid_date.setter
    def expect_bid_date(self, value):
        self._expect_bid_date = value
    @property
    def expect_sign_date(self):
        return self._expect_sign_date

    @expect_sign_date.setter
    def expect_sign_date(self, value):
        self._expect_sign_date = value
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    @property
    def is_bid(self):
        return self._is_bid

    @is_bid.setter
    def is_bid(self, value):
        self._is_bid = value
    @property
    def is_issue_for_bid(self):
        return self._is_issue_for_bid

    @is_issue_for_bid.setter
    def is_issue_for_bid(self, value):
        self._is_issue_for_bid = value
    @property
    def leads_code(self):
        return self._leads_code

    @leads_code.setter
    def leads_code(self, value):
        self._leads_code = value
    @property
    def leads_source_partner_id(self):
        return self._leads_source_partner_id

    @leads_source_partner_id.setter
    def leads_source_partner_id(self, value):
        self._leads_source_partner_id = value
    @property
    def other_partner_pid_list(self):
        return self._other_partner_pid_list

    @other_partner_pid_list.setter
    def other_partner_pid_list(self, value):
        if isinstance(value, list):
            self._other_partner_pid_list = list()
            for i in value:
                self._other_partner_pid_list.append(i)
    @property
    def other_party_sign_subject(self):
        return self._other_party_sign_subject

    @other_party_sign_subject.setter
    def other_party_sign_subject(self, value):
        self._other_party_sign_subject = value
    @property
    def other_party_sign_subject_id(self):
        return self._other_party_sign_subject_id

    @other_party_sign_subject_id.setter
    def other_party_sign_subject_id(self, value):
        self._other_party_sign_subject_id = value
    @property
    def our_sign_subject(self):
        return self._our_sign_subject

    @our_sign_subject.setter
    def our_sign_subject(self, value):
        self._our_sign_subject = value
    @property
    def partner_id(self):
        return self._partner_id

    @partner_id.setter
    def partner_id(self, value):
        self._partner_id = value
    @property
    def partner_name(self):
        return self._partner_name

    @partner_name.setter
    def partner_name(self, value):
        self._partner_name = value
    @property
    def predict_clusters_storage_capacity(self):
        return self._predict_clusters_storage_capacity

    @predict_clusters_storage_capacity.setter
    def predict_clusters_storage_capacity(self, value):
        self._predict_clusters_storage_capacity = value
    @property
    def predict_clusters_storage_unit(self):
        return self._predict_clusters_storage_unit

    @predict_clusters_storage_unit.setter
    def predict_clusters_storage_unit(self, value):
        self._predict_clusters_storage_unit = value
    @property
    def predict_clusters_units_count(self):
        return self._predict_clusters_units_count

    @predict_clusters_units_count.setter
    def predict_clusters_units_count(self, value):
        self._predict_clusters_units_count = value
    @property
    def predict_instance_core_count(self):
        return self._predict_instance_core_count

    @predict_instance_core_count.setter
    def predict_instance_core_count(self, value):
        self._predict_instance_core_count = value
    @property
    def product_family(self):
        return self._product_family

    @product_family.setter
    def product_family(self, value):
        self._product_family = value
    @property
    def project_name(self):
        return self._project_name

    @project_name.setter
    def project_name(self, value):
        self._project_name = value
    @property
    def project_phase(self):
        return self._project_phase

    @project_phase.setter
    def project_phase(self, value):
        self._project_phase = value
    @property
    def record_list(self):
        return self._record_list

    @record_list.setter
    def record_list(self, value):
        if isinstance(value, list):
            self._record_list = list()
            for i in value:
                if isinstance(i, FxiaokeCreateOrUpdateLeadsPredictRecordItemRequest):
                    self._record_list.append(i)
                else:
                    self._record_list.append(FxiaokeCreateOrUpdateLeadsPredictRecordItemRequest.from_alipay_dict(i))
    @property
    def related_leads_id(self):
        return self._related_leads_id

    @related_leads_id.setter
    def related_leads_id(self, value):
        self._related_leads_id = value
    @property
    def resource_foundation(self):
        return self._resource_foundation

    @resource_foundation.setter
    def resource_foundation(self, value):
        self._resource_foundation = value
    @property
    def sign_path(self):
        return self._sign_path

    @sign_path.setter
    def sign_path(self, value):
        self._sign_path = value
    @property
    def sign_probability(self):
        return self._sign_probability

    @sign_probability.setter
    def sign_probability(self, value):
        self._sign_probability = value
    @property
    def software_subscription_years_expand_ten(self):
        return self._software_subscription_years_expand_ten

    @software_subscription_years_expand_ten.setter
    def software_subscription_years_expand_ten(self, value):
        self._software_subscription_years_expand_ten = value
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.actual_lead_party:
            if hasattr(self.actual_lead_party, 'to_alipay_dict'):
                params['actual_lead_party'] = self.actual_lead_party.to_alipay_dict()
            else:
                params['actual_lead_party'] = self.actual_lead_party
        if self.ali_cloud_bpid_list:
            if hasattr(self.ali_cloud_bpid_list, 'to_alipay_dict'):
                params['ali_cloud_bpid_list'] = self.ali_cloud_bpid_list.to_alipay_dict()
            else:
                params['ali_cloud_bpid_list'] = self.ali_cloud_bpid_list
        if self.bid_type:
            if hasattr(self.bid_type, 'to_alipay_dict'):
                params['bid_type'] = self.bid_type.to_alipay_dict()
            else:
                params['bid_type'] = self.bid_type
        if self.cbm_work_no_list:
            if isinstance(self.cbm_work_no_list, list):
                for i in range(0, len(self.cbm_work_no_list)):
                    element = self.cbm_work_no_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.cbm_work_no_list[i] = element.to_alipay_dict()
            if hasattr(self.cbm_work_no_list, 'to_alipay_dict'):
                params['cbm_work_no_list'] = self.cbm_work_no_list.to_alipay_dict()
            else:
                params['cbm_work_no_list'] = self.cbm_work_no_list
        if self.cloud_platform_region:
            if hasattr(self.cloud_platform_region, 'to_alipay_dict'):
                params['cloud_platform_region'] = self.cloud_platform_region.to_alipay_dict()
            else:
                params['cloud_platform_region'] = self.cloud_platform_region
        if self.creator:
            if hasattr(self.creator, 'to_alipay_dict'):
                params['creator'] = self.creator.to_alipay_dict()
            else:
                params['creator'] = self.creator
        if self.crm_customer_id:
            if hasattr(self.crm_customer_id, 'to_alipay_dict'):
                params['crm_customer_id'] = self.crm_customer_id.to_alipay_dict()
            else:
                params['crm_customer_id'] = self.crm_customer_id
        if self.crm_customer_industry:
            if hasattr(self.crm_customer_industry, 'to_alipay_dict'):
                params['crm_customer_industry'] = self.crm_customer_industry.to_alipay_dict()
            else:
                params['crm_customer_industry'] = self.crm_customer_industry
        if self.crm_customer_name:
            if hasattr(self.crm_customer_name, 'to_alipay_dict'):
                params['crm_customer_name'] = self.crm_customer_name.to_alipay_dict()
            else:
                params['crm_customer_name'] = self.crm_customer_name
        if self.customer_id:
            if hasattr(self.customer_id, 'to_alipay_dict'):
                params['customer_id'] = self.customer_id.to_alipay_dict()
            else:
                params['customer_id'] = self.customer_id
        if self.deploy_platform:
            if hasattr(self.deploy_platform, 'to_alipay_dict'):
                params['deploy_platform'] = self.deploy_platform.to_alipay_dict()
            else:
                params['deploy_platform'] = self.deploy_platform
        if self.deploy_type:
            if hasattr(self.deploy_type, 'to_alipay_dict'):
                params['deploy_type'] = self.deploy_type.to_alipay_dict()
            else:
                params['deploy_type'] = self.deploy_type
        if self.expect_bid_date:
            if hasattr(self.expect_bid_date, 'to_alipay_dict'):
                params['expect_bid_date'] = self.expect_bid_date.to_alipay_dict()
            else:
                params['expect_bid_date'] = self.expect_bid_date
        if self.expect_sign_date:
            if hasattr(self.expect_sign_date, 'to_alipay_dict'):
                params['expect_sign_date'] = self.expect_sign_date.to_alipay_dict()
            else:
                params['expect_sign_date'] = self.expect_sign_date
        if self.id:
            if hasattr(self.id, 'to_alipay_dict'):
                params['id'] = self.id.to_alipay_dict()
            else:
                params['id'] = self.id
        if self.is_bid:
            if hasattr(self.is_bid, 'to_alipay_dict'):
                params['is_bid'] = self.is_bid.to_alipay_dict()
            else:
                params['is_bid'] = self.is_bid
        if self.is_issue_for_bid:
            if hasattr(self.is_issue_for_bid, 'to_alipay_dict'):
                params['is_issue_for_bid'] = self.is_issue_for_bid.to_alipay_dict()
            else:
                params['is_issue_for_bid'] = self.is_issue_for_bid
        if self.leads_code:
            if hasattr(self.leads_code, 'to_alipay_dict'):
                params['leads_code'] = self.leads_code.to_alipay_dict()
            else:
                params['leads_code'] = self.leads_code
        if self.leads_source_partner_id:
            if hasattr(self.leads_source_partner_id, 'to_alipay_dict'):
                params['leads_source_partner_id'] = self.leads_source_partner_id.to_alipay_dict()
            else:
                params['leads_source_partner_id'] = self.leads_source_partner_id
        if self.other_partner_pid_list:
            if isinstance(self.other_partner_pid_list, list):
                for i in range(0, len(self.other_partner_pid_list)):
                    element = self.other_partner_pid_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.other_partner_pid_list[i] = element.to_alipay_dict()
            if hasattr(self.other_partner_pid_list, 'to_alipay_dict'):
                params['other_partner_pid_list'] = self.other_partner_pid_list.to_alipay_dict()
            else:
                params['other_partner_pid_list'] = self.other_partner_pid_list
        if self.other_party_sign_subject:
            if hasattr(self.other_party_sign_subject, 'to_alipay_dict'):
                params['other_party_sign_subject'] = self.other_party_sign_subject.to_alipay_dict()
            else:
                params['other_party_sign_subject'] = self.other_party_sign_subject
        if self.other_party_sign_subject_id:
            if hasattr(self.other_party_sign_subject_id, 'to_alipay_dict'):
                params['other_party_sign_subject_id'] = self.other_party_sign_subject_id.to_alipay_dict()
            else:
                params['other_party_sign_subject_id'] = self.other_party_sign_subject_id
        if self.our_sign_subject:
            if hasattr(self.our_sign_subject, 'to_alipay_dict'):
                params['our_sign_subject'] = self.our_sign_subject.to_alipay_dict()
            else:
                params['our_sign_subject'] = self.our_sign_subject
        if self.partner_id:
            if hasattr(self.partner_id, 'to_alipay_dict'):
                params['partner_id'] = self.partner_id.to_alipay_dict()
            else:
                params['partner_id'] = self.partner_id
        if self.partner_name:
            if hasattr(self.partner_name, 'to_alipay_dict'):
                params['partner_name'] = self.partner_name.to_alipay_dict()
            else:
                params['partner_name'] = self.partner_name
        if self.predict_clusters_storage_capacity:
            if hasattr(self.predict_clusters_storage_capacity, 'to_alipay_dict'):
                params['predict_clusters_storage_capacity'] = self.predict_clusters_storage_capacity.to_alipay_dict()
            else:
                params['predict_clusters_storage_capacity'] = self.predict_clusters_storage_capacity
        if self.predict_clusters_storage_unit:
            if hasattr(self.predict_clusters_storage_unit, 'to_alipay_dict'):
                params['predict_clusters_storage_unit'] = self.predict_clusters_storage_unit.to_alipay_dict()
            else:
                params['predict_clusters_storage_unit'] = self.predict_clusters_storage_unit
        if self.predict_clusters_units_count:
            if hasattr(self.predict_clusters_units_count, 'to_alipay_dict'):
                params['predict_clusters_units_count'] = self.predict_clusters_units_count.to_alipay_dict()
            else:
                params['predict_clusters_units_count'] = self.predict_clusters_units_count
        if self.predict_instance_core_count:
            if hasattr(self.predict_instance_core_count, 'to_alipay_dict'):
                params['predict_instance_core_count'] = self.predict_instance_core_count.to_alipay_dict()
            else:
                params['predict_instance_core_count'] = self.predict_instance_core_count
        if self.product_family:
            if hasattr(self.product_family, 'to_alipay_dict'):
                params['product_family'] = self.product_family.to_alipay_dict()
            else:
                params['product_family'] = self.product_family
        if self.project_name:
            if hasattr(self.project_name, 'to_alipay_dict'):
                params['project_name'] = self.project_name.to_alipay_dict()
            else:
                params['project_name'] = self.project_name
        if self.project_phase:
            if hasattr(self.project_phase, 'to_alipay_dict'):
                params['project_phase'] = self.project_phase.to_alipay_dict()
            else:
                params['project_phase'] = self.project_phase
        if self.record_list:
            if isinstance(self.record_list, list):
                for i in range(0, len(self.record_list)):
                    element = self.record_list[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.record_list[i] = element.to_alipay_dict()
            if hasattr(self.record_list, 'to_alipay_dict'):
                params['record_list'] = self.record_list.to_alipay_dict()
            else:
                params['record_list'] = self.record_list
        if self.related_leads_id:
            if hasattr(self.related_leads_id, 'to_alipay_dict'):
                params['related_leads_id'] = self.related_leads_id.to_alipay_dict()
            else:
                params['related_leads_id'] = self.related_leads_id
        if self.resource_foundation:
            if hasattr(self.resource_foundation, 'to_alipay_dict'):
                params['resource_foundation'] = self.resource_foundation.to_alipay_dict()
            else:
                params['resource_foundation'] = self.resource_foundation
        if self.sign_path:
            if hasattr(self.sign_path, 'to_alipay_dict'):
                params['sign_path'] = self.sign_path.to_alipay_dict()
            else:
                params['sign_path'] = self.sign_path
        if self.sign_probability:
            if hasattr(self.sign_probability, 'to_alipay_dict'):
                params['sign_probability'] = self.sign_probability.to_alipay_dict()
            else:
                params['sign_probability'] = self.sign_probability
        if self.software_subscription_years_expand_ten:
            if hasattr(self.software_subscription_years_expand_ten, 'to_alipay_dict'):
                params['software_subscription_years_expand_ten'] = self.software_subscription_years_expand_ten.to_alipay_dict()
            else:
                params['software_subscription_years_expand_ten'] = self.software_subscription_years_expand_ten
        if self.source:
            if hasattr(self.source, 'to_alipay_dict'):
                params['source'] = self.source.to_alipay_dict()
            else:
                params['source'] = self.source
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FxiaokeCreateLeadsParams()
        if 'actual_lead_party' in d:
            o.actual_lead_party = d['actual_lead_party']
        if 'ali_cloud_bpid_list' in d:
            o.ali_cloud_bpid_list = d['ali_cloud_bpid_list']
        if 'bid_type' in d:
            o.bid_type = d['bid_type']
        if 'cbm_work_no_list' in d:
            o.cbm_work_no_list = d['cbm_work_no_list']
        if 'cloud_platform_region' in d:
            o.cloud_platform_region = d['cloud_platform_region']
        if 'creator' in d:
            o.creator = d['creator']
        if 'crm_customer_id' in d:
            o.crm_customer_id = d['crm_customer_id']
        if 'crm_customer_industry' in d:
            o.crm_customer_industry = d['crm_customer_industry']
        if 'crm_customer_name' in d:
            o.crm_customer_name = d['crm_customer_name']
        if 'customer_id' in d:
            o.customer_id = d['customer_id']
        if 'deploy_platform' in d:
            o.deploy_platform = d['deploy_platform']
        if 'deploy_type' in d:
            o.deploy_type = d['deploy_type']
        if 'expect_bid_date' in d:
            o.expect_bid_date = d['expect_bid_date']
        if 'expect_sign_date' in d:
            o.expect_sign_date = d['expect_sign_date']
        if 'id' in d:
            o.id = d['id']
        if 'is_bid' in d:
            o.is_bid = d['is_bid']
        if 'is_issue_for_bid' in d:
            o.is_issue_for_bid = d['is_issue_for_bid']
        if 'leads_code' in d:
            o.leads_code = d['leads_code']
        if 'leads_source_partner_id' in d:
            o.leads_source_partner_id = d['leads_source_partner_id']
        if 'other_partner_pid_list' in d:
            o.other_partner_pid_list = d['other_partner_pid_list']
        if 'other_party_sign_subject' in d:
            o.other_party_sign_subject = d['other_party_sign_subject']
        if 'other_party_sign_subject_id' in d:
            o.other_party_sign_subject_id = d['other_party_sign_subject_id']
        if 'our_sign_subject' in d:
            o.our_sign_subject = d['our_sign_subject']
        if 'partner_id' in d:
            o.partner_id = d['partner_id']
        if 'partner_name' in d:
            o.partner_name = d['partner_name']
        if 'predict_clusters_storage_capacity' in d:
            o.predict_clusters_storage_capacity = d['predict_clusters_storage_capacity']
        if 'predict_clusters_storage_unit' in d:
            o.predict_clusters_storage_unit = d['predict_clusters_storage_unit']
        if 'predict_clusters_units_count' in d:
            o.predict_clusters_units_count = d['predict_clusters_units_count']
        if 'predict_instance_core_count' in d:
            o.predict_instance_core_count = d['predict_instance_core_count']
        if 'product_family' in d:
            o.product_family = d['product_family']
        if 'project_name' in d:
            o.project_name = d['project_name']
        if 'project_phase' in d:
            o.project_phase = d['project_phase']
        if 'record_list' in d:
            o.record_list = d['record_list']
        if 'related_leads_id' in d:
            o.related_leads_id = d['related_leads_id']
        if 'resource_foundation' in d:
            o.resource_foundation = d['resource_foundation']
        if 'sign_path' in d:
            o.sign_path = d['sign_path']
        if 'sign_probability' in d:
            o.sign_probability = d['sign_probability']
        if 'software_subscription_years_expand_ten' in d:
            o.software_subscription_years_expand_ten = d['software_subscription_years_expand_ten']
        if 'source' in d:
            o.source = d['source']
        if 'type' in d:
            o.type = d['type']
        return o



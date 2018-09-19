#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.EduAgeDemand import EduAgeDemand
from alipay.aop.api.domain.EduSourceInfo import EduSourceInfo
from alipay.aop.api.domain.EduWorkAddress import EduWorkAddress


class AlipayEcoEduJzPostPublishModel(object):

    def __init__(self):
        self._age_demand = None
        self._commission = None
        self._company_contact = None
        self._company_logo = None
        self._company_name = None
        self._contact_phone = None
        self._date_end = None
        self._date_start = None
        self._deadline = None
        self._gender = None
        self._hire_number = None
        self._is_commission = None
        self._job_desc = None
        self._job_type = None
        self._part_time_type = None
        self._payment = None
        self._payment_remark = None
        self._payment_type = None
        self._salary = None
        self._salary_unit = None
        self._service_post_id = None
        self._source_info = None
        self._special_demand = None
        self._title = None
        self._welfare = None
        self._work_address = None
        self._work_time_remark = None
        self._working_hours = None

    @property
    def age_demand(self):
        return self._age_demand

    @age_demand.setter
    def age_demand(self, value):
        if isinstance(value, EduAgeDemand):
            self._age_demand = value
        else:
            self._age_demand = EduAgeDemand.from_alipay_dict(value)
    @property
    def commission(self):
        return self._commission

    @commission.setter
    def commission(self, value):
        self._commission = value
    @property
    def company_contact(self):
        return self._company_contact

    @company_contact.setter
    def company_contact(self, value):
        self._company_contact = value
    @property
    def company_logo(self):
        return self._company_logo

    @company_logo.setter
    def company_logo(self, value):
        self._company_logo = value
    @property
    def company_name(self):
        return self._company_name

    @company_name.setter
    def company_name(self, value):
        self._company_name = value
    @property
    def contact_phone(self):
        return self._contact_phone

    @contact_phone.setter
    def contact_phone(self, value):
        self._contact_phone = value
    @property
    def date_end(self):
        return self._date_end

    @date_end.setter
    def date_end(self, value):
        self._date_end = value
    @property
    def date_start(self):
        return self._date_start

    @date_start.setter
    def date_start(self, value):
        self._date_start = value
    @property
    def deadline(self):
        return self._deadline

    @deadline.setter
    def deadline(self, value):
        self._deadline = value
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        self._gender = value
    @property
    def hire_number(self):
        return self._hire_number

    @hire_number.setter
    def hire_number(self, value):
        self._hire_number = value
    @property
    def is_commission(self):
        return self._is_commission

    @is_commission.setter
    def is_commission(self, value):
        self._is_commission = value
    @property
    def job_desc(self):
        return self._job_desc

    @job_desc.setter
    def job_desc(self, value):
        self._job_desc = value
    @property
    def job_type(self):
        return self._job_type

    @job_type.setter
    def job_type(self, value):
        self._job_type = value
    @property
    def part_time_type(self):
        return self._part_time_type

    @part_time_type.setter
    def part_time_type(self, value):
        self._part_time_type = value
    @property
    def payment(self):
        return self._payment

    @payment.setter
    def payment(self, value):
        self._payment = value
    @property
    def payment_remark(self):
        return self._payment_remark

    @payment_remark.setter
    def payment_remark(self, value):
        self._payment_remark = value
    @property
    def payment_type(self):
        return self._payment_type

    @payment_type.setter
    def payment_type(self, value):
        self._payment_type = value
    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value
    @property
    def salary_unit(self):
        return self._salary_unit

    @salary_unit.setter
    def salary_unit(self, value):
        self._salary_unit = value
    @property
    def service_post_id(self):
        return self._service_post_id

    @service_post_id.setter
    def service_post_id(self, value):
        self._service_post_id = value
    @property
    def source_info(self):
        return self._source_info

    @source_info.setter
    def source_info(self, value):
        if isinstance(value, EduSourceInfo):
            self._source_info = value
        else:
            self._source_info = EduSourceInfo.from_alipay_dict(value)
    @property
    def special_demand(self):
        return self._special_demand

    @special_demand.setter
    def special_demand(self, value):
        if isinstance(value, list):
            self._special_demand = list()
            for i in value:
                self._special_demand.append(i)
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
    @property
    def welfare(self):
        return self._welfare

    @welfare.setter
    def welfare(self, value):
        if isinstance(value, list):
            self._welfare = list()
            for i in value:
                self._welfare.append(i)
    @property
    def work_address(self):
        return self._work_address

    @work_address.setter
    def work_address(self, value):
        if isinstance(value, list):
            self._work_address = list()
            for i in value:
                if isinstance(i, EduWorkAddress):
                    self._work_address.append(i)
                else:
                    self._work_address.append(EduWorkAddress.from_alipay_dict(i))
    @property
    def work_time_remark(self):
        return self._work_time_remark

    @work_time_remark.setter
    def work_time_remark(self, value):
        self._work_time_remark = value
    @property
    def working_hours(self):
        return self._working_hours

    @working_hours.setter
    def working_hours(self, value):
        self._working_hours = value


    def to_alipay_dict(self):
        params = dict()
        if self.age_demand:
            if hasattr(self.age_demand, 'to_alipay_dict'):
                params['age_demand'] = self.age_demand.to_alipay_dict()
            else:
                params['age_demand'] = self.age_demand
        if self.commission:
            if hasattr(self.commission, 'to_alipay_dict'):
                params['commission'] = self.commission.to_alipay_dict()
            else:
                params['commission'] = self.commission
        if self.company_contact:
            if hasattr(self.company_contact, 'to_alipay_dict'):
                params['company_contact'] = self.company_contact.to_alipay_dict()
            else:
                params['company_contact'] = self.company_contact
        if self.company_logo:
            if hasattr(self.company_logo, 'to_alipay_dict'):
                params['company_logo'] = self.company_logo.to_alipay_dict()
            else:
                params['company_logo'] = self.company_logo
        if self.company_name:
            if hasattr(self.company_name, 'to_alipay_dict'):
                params['company_name'] = self.company_name.to_alipay_dict()
            else:
                params['company_name'] = self.company_name
        if self.contact_phone:
            if hasattr(self.contact_phone, 'to_alipay_dict'):
                params['contact_phone'] = self.contact_phone.to_alipay_dict()
            else:
                params['contact_phone'] = self.contact_phone
        if self.date_end:
            if hasattr(self.date_end, 'to_alipay_dict'):
                params['date_end'] = self.date_end.to_alipay_dict()
            else:
                params['date_end'] = self.date_end
        if self.date_start:
            if hasattr(self.date_start, 'to_alipay_dict'):
                params['date_start'] = self.date_start.to_alipay_dict()
            else:
                params['date_start'] = self.date_start
        if self.deadline:
            if hasattr(self.deadline, 'to_alipay_dict'):
                params['deadline'] = self.deadline.to_alipay_dict()
            else:
                params['deadline'] = self.deadline
        if self.gender:
            if hasattr(self.gender, 'to_alipay_dict'):
                params['gender'] = self.gender.to_alipay_dict()
            else:
                params['gender'] = self.gender
        if self.hire_number:
            if hasattr(self.hire_number, 'to_alipay_dict'):
                params['hire_number'] = self.hire_number.to_alipay_dict()
            else:
                params['hire_number'] = self.hire_number
        if self.is_commission:
            if hasattr(self.is_commission, 'to_alipay_dict'):
                params['is_commission'] = self.is_commission.to_alipay_dict()
            else:
                params['is_commission'] = self.is_commission
        if self.job_desc:
            if hasattr(self.job_desc, 'to_alipay_dict'):
                params['job_desc'] = self.job_desc.to_alipay_dict()
            else:
                params['job_desc'] = self.job_desc
        if self.job_type:
            if hasattr(self.job_type, 'to_alipay_dict'):
                params['job_type'] = self.job_type.to_alipay_dict()
            else:
                params['job_type'] = self.job_type
        if self.part_time_type:
            if hasattr(self.part_time_type, 'to_alipay_dict'):
                params['part_time_type'] = self.part_time_type.to_alipay_dict()
            else:
                params['part_time_type'] = self.part_time_type
        if self.payment:
            if hasattr(self.payment, 'to_alipay_dict'):
                params['payment'] = self.payment.to_alipay_dict()
            else:
                params['payment'] = self.payment
        if self.payment_remark:
            if hasattr(self.payment_remark, 'to_alipay_dict'):
                params['payment_remark'] = self.payment_remark.to_alipay_dict()
            else:
                params['payment_remark'] = self.payment_remark
        if self.payment_type:
            if hasattr(self.payment_type, 'to_alipay_dict'):
                params['payment_type'] = self.payment_type.to_alipay_dict()
            else:
                params['payment_type'] = self.payment_type
        if self.salary:
            if hasattr(self.salary, 'to_alipay_dict'):
                params['salary'] = self.salary.to_alipay_dict()
            else:
                params['salary'] = self.salary
        if self.salary_unit:
            if hasattr(self.salary_unit, 'to_alipay_dict'):
                params['salary_unit'] = self.salary_unit.to_alipay_dict()
            else:
                params['salary_unit'] = self.salary_unit
        if self.service_post_id:
            if hasattr(self.service_post_id, 'to_alipay_dict'):
                params['service_post_id'] = self.service_post_id.to_alipay_dict()
            else:
                params['service_post_id'] = self.service_post_id
        if self.source_info:
            if hasattr(self.source_info, 'to_alipay_dict'):
                params['source_info'] = self.source_info.to_alipay_dict()
            else:
                params['source_info'] = self.source_info
        if self.special_demand:
            if isinstance(self.special_demand, list):
                for i in range(0, len(self.special_demand)):
                    element = self.special_demand[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.special_demand[i] = element.to_alipay_dict()
            if hasattr(self.special_demand, 'to_alipay_dict'):
                params['special_demand'] = self.special_demand.to_alipay_dict()
            else:
                params['special_demand'] = self.special_demand
        if self.title:
            if hasattr(self.title, 'to_alipay_dict'):
                params['title'] = self.title.to_alipay_dict()
            else:
                params['title'] = self.title
        if self.welfare:
            if isinstance(self.welfare, list):
                for i in range(0, len(self.welfare)):
                    element = self.welfare[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.welfare[i] = element.to_alipay_dict()
            if hasattr(self.welfare, 'to_alipay_dict'):
                params['welfare'] = self.welfare.to_alipay_dict()
            else:
                params['welfare'] = self.welfare
        if self.work_address:
            if isinstance(self.work_address, list):
                for i in range(0, len(self.work_address)):
                    element = self.work_address[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.work_address[i] = element.to_alipay_dict()
            if hasattr(self.work_address, 'to_alipay_dict'):
                params['work_address'] = self.work_address.to_alipay_dict()
            else:
                params['work_address'] = self.work_address
        if self.work_time_remark:
            if hasattr(self.work_time_remark, 'to_alipay_dict'):
                params['work_time_remark'] = self.work_time_remark.to_alipay_dict()
            else:
                params['work_time_remark'] = self.work_time_remark
        if self.working_hours:
            if hasattr(self.working_hours, 'to_alipay_dict'):
                params['working_hours'] = self.working_hours.to_alipay_dict()
            else:
                params['working_hours'] = self.working_hours
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayEcoEduJzPostPublishModel()
        if 'age_demand' in d:
            o.age_demand = d['age_demand']
        if 'commission' in d:
            o.commission = d['commission']
        if 'company_contact' in d:
            o.company_contact = d['company_contact']
        if 'company_logo' in d:
            o.company_logo = d['company_logo']
        if 'company_name' in d:
            o.company_name = d['company_name']
        if 'contact_phone' in d:
            o.contact_phone = d['contact_phone']
        if 'date_end' in d:
            o.date_end = d['date_end']
        if 'date_start' in d:
            o.date_start = d['date_start']
        if 'deadline' in d:
            o.deadline = d['deadline']
        if 'gender' in d:
            o.gender = d['gender']
        if 'hire_number' in d:
            o.hire_number = d['hire_number']
        if 'is_commission' in d:
            o.is_commission = d['is_commission']
        if 'job_desc' in d:
            o.job_desc = d['job_desc']
        if 'job_type' in d:
            o.job_type = d['job_type']
        if 'part_time_type' in d:
            o.part_time_type = d['part_time_type']
        if 'payment' in d:
            o.payment = d['payment']
        if 'payment_remark' in d:
            o.payment_remark = d['payment_remark']
        if 'payment_type' in d:
            o.payment_type = d['payment_type']
        if 'salary' in d:
            o.salary = d['salary']
        if 'salary_unit' in d:
            o.salary_unit = d['salary_unit']
        if 'service_post_id' in d:
            o.service_post_id = d['service_post_id']
        if 'source_info' in d:
            o.source_info = d['source_info']
        if 'special_demand' in d:
            o.special_demand = d['special_demand']
        if 'title' in d:
            o.title = d['title']
        if 'welfare' in d:
            o.welfare = d['welfare']
        if 'work_address' in d:
            o.work_address = d['work_address']
        if 'work_time_remark' in d:
            o.work_time_remark = d['work_time_remark']
        if 'working_hours' in d:
            o.working_hours = d['working_hours']
        return o



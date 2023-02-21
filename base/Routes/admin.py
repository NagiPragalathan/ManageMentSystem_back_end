# Reguler and spl Functions
import datetime, json, openpyxl, mimetypes, os

# DB Tables imports
from .models import ( Gallery,Team,logo,Carrer,blog,Testimonials,Events,HowWeWork,Birac,Tbi,DemoDayTOPSECTION,DemoDayPic,
                    CategoryforGallery,CentralGovernmentFundingDB,ContactEditPage,fishieries,EDI_TOPSECTION,SamridthFund,Start_UpTN,StateGovtFund,
                    CategoryforTeams,OurStartup,Investors,AboutHeading,MBADB,Govt_Tie,LastContent,UploadImage,GlobalMarket,GlobalMarketPic,
                    CategoryforEvents,FooterEditPage,SocialMediaLinks,EDI_Overview_Section,MeitY_SAMRIDH,Start_UpTNContent2,StateGovtFundSecondSection,
                    CategoryforQualification,International_Partners,Sisfs,WhoAreWe,Contact_SECTION,HOME_TESTIMONIAL,EventsForm,Facilities_developed,About_SISFS,
                    CategoryforExperience,EDI_InnovationVoucher,EDI_WeAimAtSection,EDI_Eligibility_Section,BundledServices,Start_UpTNimg1,Start_UpTNimg2,
                    CategoryforBlogs,StateGovtFundEligibilitySection,MentorConnectDB,MentorClinicDB, angelInvestorDB, new_venturesDB,TOPSECTION,WhatWeDo,
                    CategoryforStartups,OurProcess,SpendingSection,JoinOurCommunity,HomePdfLink )

# Custom Tools Functions
from .Tools import get_images,get_team,reguler_datas,get_blog,get_startup,get_DemoDayPic,freguler_datas

# Django Functions 
from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required





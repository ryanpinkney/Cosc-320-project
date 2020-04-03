import java.util.Scanner;
import java.io.*;
import java.util.concurrent.TimeUnit;
import java.util.ArrayList;

public class Team_project {
	
	
	//This is the main class which imports data and calls the algorithms
	public static void main(String[] args) throws Exception {
		
		//reading the csv files with the data on likes and dislikes
		//this obtains data on the first user who will be given recommendations
		File file1 = new File("Data_3.csv");
		
		BufferedReader users = new BufferedReader(new FileReader(file1));
		
		//arraylist holds the important user and another for the people he will compare to
		ArrayList User1 = new ArrayList();
		ArrayList toCompare = new ArrayList();
		ArrayList recommendations = new ArrayList();
		
		//code ignores the titles at top of data list and handles preparation for loop
		String skipTitles = users.readLine();
		
		String line = users.readLine();
		String splitter[] = line.split(",", 3);
		String userName = splitter[0];
		String thingOpinion[] = {splitter[1], splitter[2]};
		User1.add(thingOpinion);
		//while loop prepare the array for the important user
		while((line = users.readLine()) != null) {
			splitter = line.split(",", 3);
			thingOpinion = new String[2];
			thingOpinion[0] = splitter[1];
			thingOpinion[1] = splitter[2];
			if(splitter[0].contentEquals(userName)) {
				User1.add(thingOpinion);
			}
			else {
				break;
			}
		}

		
		userName = splitter[0];
		ArrayList temporary = new ArrayList();
		//next while loop prepares the tocompare list with a single user, then compares, then prepares the next tocompare user
		while((line != null)){
			//this while loop prepares fills toCompare with a single users interests
			while(userName.contentEquals(splitter[0]) && line != null) {
				thingOpinion = new String[2];
				thingOpinion[0] = splitter[1]; 
				thingOpinion[1]	= splitter[2];
				toCompare.add(thingOpinion);
				line = users.readLine();
				if(line != null) {
					splitter = line.split(",", 3);
				}
			}
			
			temporary = algorithmAforProject3(User1, toCompare);
			temporary = algorithmBforProject3(User1, toCompare);
			
			if(temporary != null) {
				for(int i = 0; i < temporary.size(); i++) {
					String element = (String) temporary.get(i);
					if(recommendations.indexOf(element) == -1) {
						recommendations.add(element);
				}
			}
			}

			toCompare.clear();
			userName = splitter[0];
		}
		
		users.close();
		
		for(int i = 0; i < recommendations.size(); i++) {
			System.out.print(recommendations.get(i) + " ");
		}
	}
	
	//this is the straightforward O(n^2) algorithm
	public static ArrayList algorithmAforProject3(ArrayList a1, ArrayList a2) throws Exception{
		
		//these are just some important variables
		long startTime = System.currentTimeMillis();
		double similarity = 0;
		double totalOpinions = 0;
		//stores the user1 opinion
		String opinion1[];
		//stores the comparison peoples opinions
		String opinion2[];
		
		//the arraylist we will store recommendations in if the two are similar
		ArrayList recommendations = new ArrayList();
		
		//flag booleans makes the for loops easier to use
		boolean flag1 = false;
		boolean flag2 = false;
		
		for(int i = 0; i < a2.size(); i++) {
			
			opinion2 = (String[]) a2.get(i);
			if(opinion2[1].contentEquals("like") || opinion2[1].contentEquals("dislike")) {
				totalOpinions++;
			}
			for(int j = 0; j < a1.size(); j++) {
				
				opinion1 = (String[]) a1.get(j);
				
				 if((opinion1[1].contentEquals("like") || opinion1[1].contentEquals("dislike")) && !flag1) {
					totalOpinions++;
				}
				
				if(opinion1[0].contentEquals(opinion2[0])) {
					flag2 = true;
					if((opinion1[1].contentEquals(opinion2[1])) && (opinion2[1].contentEquals("like") || opinion2[1].contentEquals("dislike"))) {
						similarity++;
						totalOpinions--;
					}
					else if(opinion1[1].contentEquals("like") && opinion2[1].contentEquals("dislike")) {
						similarity--;
						totalOpinions--;
					}
					else if(opinion2[1].contentEquals("like") && opinion1[1].contentEquals("dislike")) {
						similarity--;
						totalOpinions--;
					}
				}
				
			}
			flag1 = true;
			if(!flag2 && opinion2[1].contentEquals("like")) {
				recommendations.add(opinion2[0]);
			}
			flag2 = false;
		}

		//calculate and output the total similarity between the users
		double totalSim = (similarity/totalOpinions) * 100;
		System.out.println("total Similarity is: " + totalSim + "%");
		

		long endTime = System.currentTimeMillis();
		long totalTime = endTime - startTime;
		System.out.println("total time was " + totalTime + " milliseconds");
		
		//final output and return values
		if(totalSim > 70) {
		System.out.println("users are similar");
		return recommendations;
		}
		System.out.println("users are not very similar");
		return null;
	}
	
	
	public static ArrayList algorithmBforProject3(ArrayList a1, ArrayList a2)throws Exception {
		//establishes important variables
		long startTime = System.currentTimeMillis();
		double similarity = 0;
		double totalOpinions = 0;
		ArrayList reccomendations = new ArrayList();
		
		mergeSort(a1);
		mergeSort(a2);
		
		for(int k = 0; k < a1.size(); k++) {
			String[] opinion = (String[]) a1.get(k);
			if(!(opinion[1].contentEquals(""))) {
				totalOpinions++;
			}
		}
		for(int k = 0; k < a2.size(); k++) {
			String[] opinion = (String[]) a2.get(k);
			if(!(opinion[1].contentEquals(""))) {
				totalOpinions++;
			}
		}
		
		int i = 0;
		int j = 0;
		String[] opinion1;
		String[] opinion2;
		boolean flag = false;
		
		while(i < a1.size() && j < a2.size()) {
			opinion1 = (String[]) a1.get(i);
			opinion2 = (String[]) a2.get(j);
			
			int comparison = opinion1[0].compareTo(opinion2[0]);
			
			if(comparison == 0) {
				flag = true;
				i++;
				j++;
				if(opinion1[1].contentEquals(opinion2[1]) && (opinion1[1].contentEquals("like") || opinion2[1].contentEquals("dislike"))){
					totalOpinions--;
					similarity++;
				}
				else if(opinion1[1].contentEquals("like") && opinion2[1].contentEquals("dislike")) {
					similarity--;
					totalOpinions--;
				}
				else if(opinion2[1].contentEquals("like") && opinion1[1].contentEquals("dislike")) {
					similarity--;
					totalOpinions--;
				}
			}
			else if (comparison > 0) {
				j++;
				if(opinion2[1].contentEquals("like")) {
					reccomendations.add(opinion2[0]);
				}	
			}
			else {
				i++;
			}
			
		}
		
		for(int k = j; j < a2.size(); j++) {
			opinion2 = (String[]) a2.get(j);
			if(opinion2[1].contentEquals("like")) {
				reccomendations.add(opinion2[0]);
			}
		}
		
		
		
		
		//final output return the reccomended list if the two are determined to be similar
		double totalSim = (similarity/totalOpinions) * 100;
		System.out.println("total Similarity is: " + totalSim + "%");
		long endTime = System.currentTimeMillis();
		long totalTime = endTime - startTime;
		System.out.println("total time was " + totalTime + "milliseconds");
		
		if(totalSim > 70) {
			System.out.println("users are similar");
			return reccomendations;
			}
			System.out.println("users are not very similar");
			return null;
		
		
		
		
	}
	//just your standard merge sort algorithm
	public static void mergeSort(ArrayList list) {
		if(list.size() >= 2) {
			int leftLength = list.size()/2;
			int rightLength = list.size() - leftLength;
			ArrayList left = new ArrayList();
			ArrayList right = new ArrayList();
			for(int i = 0; i < leftLength; i++) {
				left.add(list.get(i));
			}
			for(int i = 0; i < rightLength; i++) {
				right.add(list.get(i + leftLength));
			}
			mergeSort(left);
			mergeSort(right);
			merge(list, left, right);
		}
	}
	//the part of the merge sort algorithm that merges the divided arrays
	public static void merge(ArrayList list, ArrayList left, ArrayList right) {
		int index1 = 0;
		int index2 = 0;
		
		/*these flags are important for preventing an index out of bounds exception caused
		 * by trying to get the next element after the last was removed
		 */
		boolean leftflag = false;
		boolean rightflag = false;
		for(int i = 0; i < list.size(); i++) {
			String[] case1 = (String[]) left.get(index1);
			String[] case2 = (String[]) right.get(index2);
			String name1 = case1[0];
			String name2 = case2[0];
			if((index2 >= right.size() || (index1 < left.size() && (name1.compareToIgnoreCase(name2)<0 || rightflag))) && !leftflag) {
				list.set(i, left.get(index1));
				index1++;
				if(index1 >= left.size()) {
					index1--;
					leftflag = true;
				}
			}
			else {
				list.set(i, right.get(index2));
				index2++;
				if(index2 >= right.size()) {
					index2--;
					rightflag = true;
				}
			}
			}
		}
	}



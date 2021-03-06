package main

import (
	"fmt"
	"log"
	"os"
	"flag"
	"path/filepath"

	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
	"k8s.io/client-go/kubernetes"
	"k8s.io/client-go/tools/clientcmd"
)

func main() {

	var (
		namespaceName = flag.String("namespace", "", "Name of the namespace from which you want to list the Pods")
	)

	flag.Parse()

	kubeconfig := filepath.Join(os.Getenv("HOME"), ".kube", "config")
	log.Println("Using kubeconfig file: ", kubeconfig)
	config, err := clientcmd.BuildConfigFromFlags("", kubeconfig)

	if err != nil {
		log.Fatal(err)
	}

	clientset, err := kubernetes.NewForConfig(config)
	if err != nil {
		log.Fatal(err)
	}

	pods, err := clientset.CoreV1().Pods(*namespaceName).List(metav1.ListOptions{})
	if err != nil {
		log.Fatal(err)
	}

	for i, pod := range pods.Items {
		if i != 1000000 {
			fmt.Println(pod.GetName())
		}
	}
}
